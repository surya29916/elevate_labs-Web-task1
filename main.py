<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Landing Page</title>
    <link rel="stylesheet" href="style.css">
</head>
<style>
    /* General Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
}

/* HEADER */
header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 10%;
    background-color: #333;
    color: white;
}

.logo {
    font-size: 1.5em;
    font-weight: bold;
}

nav ul {
    list-style: none;
    display: flex;
    gap: 20px;
}

nav ul li a {
    color: white;
    text-decoration: none;
}

.menu-toggle {
    display: none;
    font-size: 1.8em;
    cursor: pointer;
}

/* HERO SECTION */
.hero {
    height: 80vh;
    background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                url('https://picsum.photos/1600/900') no-repeat center/cover;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: white;
    padding: 20px;
}

.hero h1 {
    font-size: 2.5em;
    margin-bottom: 10px;
}

.hero p {
    font-size: 1.2em;
    margin-bottom: 20px;
}

.btn {
    padding: 10px 20px;
    background-color: orange;
    color: white;
    text-decoration: none;
    border-radius: 5px;
}

/* FOOTER */
footer {
    background-color: #222;
    color: white;
    text-align: center;
    padding: 15px;
}

footer a {
    color: orange;
    text-decoration: none;
}

/* RESPONSIVENESS */
@media (max-width: 768px) {
    nav ul {
        flex-direction: column;
        position: absolute;
        top: 60px;
        right: 10%;
        background-color: #333;
        width: 200px;
        display: none;
        padding: 10px;
    }

    nav ul.active {
        display: flex;
    }

    .menu-toggle {
        display: block;
    }
}

    </style>
<body>

    <!-- HEADER -->
    <header>
        <div class="logo">MyLogo</div>
        <nav>
            <ul class="nav-links">
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Services</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
            <div class="menu-toggle">&#9776;</div>
        </nav>
    </header>

    <!-- HERO SECTION -->
    <section class="hero">
        <div class="hero-content">
            <h1>Welcome to Our Landing Page</h1>
            <p>Your journey to success starts here. We help you achieve your goals with modern solutions.</p>
            <a href="#" class="btn">Get Started</a>
        </div>
    </section>

    <!-- FOOTER -->
    <footer>
        <p>&copy; 2025 MyWebsite. All Rights Reserved.</p>
        <div class="social-links">
            <a href="#">Facebook</a> |
            <a href="#">Twitter</a> |
            <a href="#">Instagram</a>
        </div>
    </footer>

    <script>
        // Mobile menu toggle
        const menuToggle = document.querySelector('.menu-toggle');
        const navLinks = document.querySelector('.nav-links');
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    </script>

</body>
</html>
