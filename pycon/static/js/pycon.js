document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('menuToggle').addEventListener('click', function() {
        document.querySelector('.nav-links').classList.toggle('active');
        // Optional: Toggle animation for hamburger icon
        this.classList.toggle('active');
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        const navbar = document.querySelector('.nav-links');
        const menuToggle = document.getElementById('menuToggle');
        
        if (!navbar.contains(event.target) && !menuToggle.contains(event.target)) {
            navbar.classList.remove('active');
            menuToggle.classList.remove('active');
        }
    });
});
