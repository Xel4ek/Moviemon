function keys() {
    const left = document.getElementById('left').getAttribute('href');
    const right = document.getElementById('right').getAttribute('href');
    const up = document.getElementById('up').getAttribute('href');
    const down = document.getElementById('down').getAttribute('href');
    const select = document.getElementById('select').getAttribute('href');
    const start = document.getElementById('start').getAttribute('href');
    const a = document.getElementById('a').getAttribute('href');
    const b = document.getElementById('b').getAttribute('href');

    document.addEventListener('keydown', (event) => {
        if (event.code === 'KeyW' || event.code === 'ArrowUp') {
            window.location.href = up;
        }
        if (event.code === 'KeyS' || event.code === 'ArrowDown') {
            window.location.href = down;
        }
        if (event.code === 'KeyA' || event.code === 'ArrowLeft') {
            window.location.href = left;
        }
        if (event.code === 'KeyD' || event.code === 'ArrowRight') {
            window.location.href = right;
        }
        if (event.code === 'Space') {
            window.location.href = a;
        }
        if (event.code === 'Enter') {
            window.location.href = select;
        }
        if (event.code === 'Backspace') {
            window.location.href = b;
        }
        if (event.code === 'Escape') {
            window.location.href = start;
        }
    })
}

window.onload = keys()