// script.js
document.querySelectorAll('.eliminar').forEach(item => {
    item.addEventListener('click', function(event) {
        if (!confirm('¿Estás seguro de que deseas eliminar este estudiante?')) {
            event.preventDefault();
        }
    });
});
