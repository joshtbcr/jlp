<script setup lang="ts">
import { ref } from 'vue'

const cedula = ref('')
const mensaje = ref('')
const showPasswordModal = ref(false)
const passwordInput = ref('')
const isLoading = ref(false)

const estadoCuentaPath = "/cuentas/generar-excel/?cedula="
const url = "https://local-dev-api.joshlepresta.com:8000"
const excelURL = url + estadoCuentaPath

function getCookie(name: string) {
  const value = `; ${document.cookie}`
  const parts = value.split(`; ${name}=`)
  if (parts.length === 2) return parts.pop()?.split(';').shift()
}

function parseJwt(token: string) {
  const base64Url = token.split('.')[1]
  const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/')
  const jsonPayload = decodeURIComponent(atob(base64).split('').map(function (c) {
    return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)
  }).join(''))
  return JSON.parse(jsonPayload)
}

async function getJwtToken(cedula: string, password: string) {
  const jwtURL = url + "/token"
  const credentials = new FormData()
  credentials.append('username', cedula)
  credentials.append('password', password)
  try {
    const response = await fetch(jwtURL, {
      method: 'POST',
      credentials: 'include',
      body: credentials
    })
    if (!response.ok) {
      mensaje.value = "Cédula o contraseña incorrecta."
      throw new Error('Login failed')
    }
    const data = await response.json()
    const token = data.access_token
    // Optionally, set the token as a cookie if your backend doesn't do it
    document.cookie = `jwt_token=${token}; path=/`
    return token
  } catch (error) {
    mensaje.value = 'Error de autenticación.'
    throw error
  }
}

async function hayTokenValido(cedulaInput: string) {
  const token = getCookie('jwt_token')
  if (!token) {
    showPasswordModal.value = true
    return false
  } else {
    try {
      const claims = parseJwt(token)
      // Optionally, check token expiration here
      return true
    } catch {
      showPasswordModal.value = true
      return false
    }
  }
}

async function descargar() {
  if (!cedula.value) {
    mensaje.value = 'Por favor ingrese un número de cédula.'
    return
  }
  mensaje.value = ''
  isLoading.value = true
  const userLogueado = await hayTokenValido(cedula.value)
  if (!userLogueado) {
    isLoading.value = false
    return
  }
  try {
    const resp = await fetch(excelURL + cedula.value, {
      method: "GET",
      headers: {
        "Content-Type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      },
      credentials: 'include'
    })
    if (!resp.ok) throw new Error('Error en la consulta')
    const blob = await resp.blob()
    const urlBlob = URL.createObjectURL(blob)
    const a = document.createElement("a")
    a.href = urlBlob
    a.download = "estado_de_cuenta.xlsx"
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    mensaje.value = 'Descarga completada.'
  } catch (error: any) {
    mensaje.value = error.message || 'Ocurrió un error al consultar el estado de cuenta.'
  } finally {
    isLoading.value = false
  }
}

async function submitPassword() {
  if (!passwordInput.value) {
    mensaje.value = 'Por favor ingrese la contraseña.'
    return
  }
  try {
    await getJwtToken(cedula.value, passwordInput.value)
    showPasswordModal.value = false
    passwordInput.value = ''
    descargar()
  } catch {
    // mensaje.value is set in getJwtToken
  }
}
</script>

<template>
  <div class="container mt-5">
    <h1 class="mb-4">Josh Le Presta</h1>
    <input
      type="text"
      class="form-control mb-2"
      placeholder="Ingresar número de cédula"
      v-model="cedula"
      @keydown.enter="descargar"
    />
    <button class="btn btn-primary w-100 mb-2" @click="descargar" :disabled="isLoading">
      {{ isLoading ? 'Consultando...' : 'Descargar estado de cuenta' }}
    </button>
    <div class="alert alert-info mt-3" v-if="mensaje">{{ mensaje }}</div>

    <!-- Password Modal -->
    <div v-if="showPasswordModal" class="modal fade show d-block" tabindex="-1" style="background:rgba(0,0,0,0.5)">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Ingresar contraseña</h5>
          </div>
          <div class="modal-body">
            <input
              type="password"
              class="form-control"
              placeholder="Contraseña"
              v-model="passwordInput"
              @keydown.enter="submitPassword"
              autofocus
            />
          </div>
          <div class="modal-footer">
            <button class="btn btn-secondary" @click="showPasswordModal = false">Cancelar</button>
            <button class="btn btn-primary" @click="submitPassword">Aceptar</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>