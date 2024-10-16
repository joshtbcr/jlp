
const estadoCuentaPath = "/cuentas/generar-excel/?cedula=";
const url = "http://127.0.0.1:8000"
const excelURL = url + estadoCuentaPath;





async function sendData() {
    const cedulaInput = document.getElementById("cedulaInput").value;
    const userLogueado = await hayTokenValido(cedulaInput);
    if (!userLogueado)
        return;
    

    try {
        fetch(excelURL+cedulaInput, {
            method: "GET",
            headers: {
                "Content-Type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            }
        })
        .then(resp => resp.blob())
        .then(blob => {
            const url = URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url;
            a.download = "estado_de_cuenta.xlsx";
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        });
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("output").innerText = "Error: " + error.message;
    }
}
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}


async function hayTokenValido(cedulaInput){
    const token = getCookie('jwt_token');
    if ((token === undefined || token === null)) {
        var passwordInput = promptForPassword();
        if(!passwordInput) return;
        await getJwtToken(cedulaInput, passwordInput);
    }
    else{
        
        console.log("token: ");
        console.log(token);
        const claims = parseJwt(token);
        console.log(claims); // Outputs the decoded payload
        return true
    }
}
function promptForPassword() {
    const password = window.prompt("Ingresar contraseña:");
    if (password) {
        console.log("Password:", password);
        return password;
    } else {
        console.log("Credentials were not entered.");
        return false;
    }
}

// Example of making a POST request to authenticate and retrieve a JWT token
async function getJwtToken(cedula,password) {
    const jwtURL = url + "/token";
    const credentials = new FormData();
    credentials.append('username', cedula); // Replace with actual username
    credentials.append('password', password); // Replace with actual password

    try {
        const response = await fetch(jwtURL, {
            method: 'POST',
            body: credentials 
        });
        if (!response.ok) {
            window.alert("Cédula o contraseña incorrecta.");
            throw new Error('Login failed');
        }
        const data = await response.json();
        const token = data.access_token;
        console.log('JWT Token:', token);

        return token; // Return the token
    } catch (error) {
        console.error('Error:', error);
    }
}
function parseJwt (token) {
    const base64Url = token.split('.')[1]; // Get the payload part
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/'); // Replace URL-safe characters
    const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
}
