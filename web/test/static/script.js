const contenedorLinea = document.getElementById('contenedor-linea');
async function actualizarLinea() {
    const response = await fetch('/stream');
    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        const linea = decoder.decode(value);
        contenedorLinea.innerHTML = linea;
    }
}
actualizarLinea();