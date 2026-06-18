html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DTeconologíaYMás | Innovación • Software • Infraestructura</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        /* --- ESTILOS GENERALES Y RESET --- */
        *, *::before, *::after {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        :root {
            --bg-primary: #07090e;
            --bg-secondary: #0d111a;
            --bg-card: #131924;
            --accent: #ff2a3b;
            --accent-glow: rgba(255, 42, 59, 0.4);
            --text-main: #f3f4f6;
            --text-muted: #9ca3af;
            --border-color: #1e293b;
            --font-family: 'Plus Jakarta Sans', sans-serif;
        }

        body {
            background-color: var(--bg-primary);
            color: var(--text-main);
            font-family: var(--font-family);
            line-height: 1.6;
            overflow-x: hidden;
        }

        a {
            text-decoration: none;
            color: inherit;
            transition: all 0.3s ease;
        }

        ul {
            list-style: none;
        }

        img {
            max-width: 100%;
            display: block;
        }

        /* --- CONTENEDORES --- */
        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 24px;
        }

        .section-padding {
            padding: 100px 0;
        }

        /* --- TITULARES --- */
        .section-header {
            text-align: center;
            margin-bottom: 60px;
        }

        .section-header h2 {
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 16px;
            letter-spacing: -0.5px;
        }

        .section-header h2 span {
            color: var(--accent);
            text-shadow: 0 0 20px var(--accent-glow);
        }

        .section-header p {
            color: var(--text-muted);
            font-size: 1.1rem;
            max-width: 600px;
            margin: 0 auto;
        }

        /* --- BOTONES --- */
        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 12px 28px;
            font-weight: 600;
            border-radius: 8px;
            gap: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 0.95rem;
        }

        .btn-primary {
            background-color: var(--accent);
            color: white;
            box-shadow: 0 4px 20px var(--accent-glow);
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 25px rgba(255, 42, 59, 0.6);
        }

        .btn-secondary {
            background-color: transparent;
            color: var(--text-main);
            border: 1px solid var(--border-color);
        }

        .btn-secondary:hover {
            background-color: rgba(255, 255, 255, 0.05);
            border-color: var(--text-muted);
            transform: translateY(-2px);
        }

        /* --- NAVBAR --- */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
            background-color: rgba(7, 9, 14, 0.8);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(30, 41, 59, 0.5);
            padding: 20px 0;
        }

        .navbar .container {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .logo-box {
            background-color: var(--accent);
            color: white;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 1.5rem;
            border-radius: 6px;
            position: relative;
        }

        .logo-box::after {
            content: '';
            position: absolute;
            width: 100%;
            height: 100%;
            border: 2px solid white;
            top: 0;
            left: 0;
            border-radius: 6px;
            transform: scale(0.8);
        }

        .logo-text h1 {
            font-size: 1.3rem;
            font-weight: 700;
            letter-spacing: -0.5px;
        }

        .logo-text h1 span {
            color: var(--accent);
        }

        .logo-text p {
            font-size: 0.65rem;
            color: var(--text-muted);
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        .nav-links {
            display: flex;
            gap: 32px;
        }

        .nav-links a {
            font-size: 0.95rem;
            font-weight: 500;
            color: var(--text-muted);
        }

        .nav-links a:hover, .nav-links a.active {
            color: var(--text-main);
        }

        /* --- HERO SECTION --- */
        .hero {
            padding-top: 180px;
            padding-bottom: 100px;
            position: relative;
            background: radial-gradient(circle at 80% 20%, rgba(255, 42, 59, 0.08) 0%, transparent 50%);
        }

        .hero-grid {
            display: grid;
            grid-template-columns: 1.2fr 0.8fr;
            gap: 60px;
            align-items: center;
        }

        .hero-content h2 {
            font-size: 3.8rem;
            font-weight: 800;
            line-height: 1.15;
            margin-bottom: 24px;
            letter-spacing: -1.5px;
        }

        .hero-content h2 span {
            color: var(--accent);
            text-shadow: 0 0 30px var(--accent-glow);
        }

        .hero-content p {
            color: var(--text-muted);
            font-size: 1.2rem;
            margin-bottom: 36px;
            max-width: 620px;
        }

        .hero-actions {
            display: flex;
            gap: 16px;
            margin-bottom: 48px;
        }

        .hero-features {
            display: flex;
            gap: 32px;
            border-top: 1px solid var(--border-color);
            padding-top: 32px;
        }

        .hero-feat-item {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 0.9rem;
            color: var(--text-muted);
        }

        .hero-feat-item i {
            color: var(--accent);
            font-size: 1.1rem;
        }

        /* Hero Abstract Visual */
        .hero-visual {
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .hero-glow-card {
            background: linear-gradient(135deg, var(--bg-card) 0%, var(--bg-secondary) 100%);
            border: 1px solid var(--border-color);
            border-radius: 24px;
            padding: 40px;
            width: 100%;
            height: 400px;
            position: relative;
            box-shadow: 0 20px 40px rgba(0,0,0,0.5);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }

        .hero-glow-card::before {
            content: '';
            position: absolute;
            width: 150px;
            height: 150px;
            background-color: var(--accent);
            filter: blur(100px);
            opacity: 0.3;
            top: 20%;
            left: 30%;
        }

        .hero-glow-card i {
            font-size: 5rem;
            color: var(--accent);
            margin-bottom: 24px;
            animation: pulse 3s infinite ease-in-out;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 0.8; }
            50% { transform: scale(1.05); opacity: 1; text-shadow: 0 0 30px var(--accent); }
        }

        /* --- STATS COUNTER --- */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 24px;
            background-color: var(--bg-secondary);
            border: 1px solid var(--border-color);
            padding: 40px;
            border-radius: 16px;
            margin-top: -20px;
            position: relative;
            z-index: 10;
        }

        .stat-item {
            text-align: center;
            border-right: 1px solid var(--border-color);
        }

        .stat-item:last-child {
            border-right: none;
        }

        .stat-number {
            font-size: 2.5rem;
            font-weight: 800;
            color: var(--text-main);
            margin-bottom: 4px;
        }

        .stat-number span {
            color: var(--accent);
        }

        .stat-label {
            color: var(--text-muted);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        /* --- SERVICES (BENTO GRID STYLE) --- */
        .services-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
        }

        .service-card {
            background-color: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 32px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .service-card:hover {
            transform: translateY(-5px);
            border-color: var(--accent);
            box-shadow: 0 10px 30px rgba(255, 42, 59, 0.05);
        }

        .service-icon {
            width: 50px;
            height: 50px;
            background-color: rgba(255, 42, 59, 0.1);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 24px;
            color: var(--accent);
            font-size: 1.4rem;
            border: 1px solid rgba(255, 42, 59, 0.2);
        }

        .service-card h3 {
            font-size: 1.3rem;
            font-weight: 700;
            margin-bottom: 12px;
        }

        .service-card p {
            color: var(--text-muted);
            font-size: 0.95rem;
            margin-bottom: 20px;
        }

        .service-link {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: var(--accent);
            font-weight: 600;
            font-size: 0.9rem;
        }

        .service-link i {
            font-size: 0.8rem;
            transition: transform 0.3s ease;
        }

        .service-card:hover .service-link i {
            transform: translateX(4px);
        }

        /* --- SOLUTIONS FOR (SECTORS) --- */
        .solutions {
            background-color: var(--bg-secondary);
        }

        .solutions-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 16px;
        }

        .solution-card {
            background-color: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 24px;
            text-align: center;
            transition: all 0.3s ease;
        }

        .solution-card:hover {
            border-color: rgba(255, 42, 59, 0.4);
            background-color: rgba(255, 42, 59, 0.02);
        }

        .solution-card i {
            font-size: 2rem;
            color: var(--accent);
            margin-bottom: 16px;
        }

        .solution-card h4 {
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 8px;
        }

        .solution-card p {
            color: var(--text-muted);
            font-size: 0.85rem;
        }

        /* --- PROCESS --- */
        .process-roadmap {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 20px;
            position: relative;
            margin-top: 40px;
        }

        .process-roadmap::before {
            content: '';
            position: absolute;
            top: 35px;
            left: 10%;
            width: 80%;
            height: 2px;
            background: linear-gradient(90deg, var(--border-color) 0%, var(--accent) 50%, var(--border-color) 100%);
            z-index: 1;
        }

        .process-step {
            text-align: center;
            position: relative;
            z-index: 2;
        }

        .step-number {
            width: 70px;
            height: 70px;
            background-color: var(--bg-card);
            border: 2px solid var(--border-color);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px;
            font-weight: 700;
            color: var(--text-muted);
            transition: all 0.3s ease;
            font-size: 1.2rem;
        }

        .process-step:hover .step-number {
            border-color: var(--accent);
            color: var(--accent);
            box-shadow: 0 0 20px var(--accent-glow);
            transform: scale(1.05);
        }

        .process-step h4 {
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 8px;
        }

        .process-step p {
            color: var(--text-muted);
            font-size: 0.85rem;
            padding: 0 10px;
        }

        /* --- TECHNOLOGIES --- */
        .tech-section {
            background-color: rgba(13, 17, 26, 0.5);
            padding: 60px 0;
            border-top: 1px solid var(--border-color);
            border-bottom: 1px solid var(--border-color);
        }

        .tech-flex {
            display: flex;
            justify-content: space-around;
            align-items: center;
            flex-wrap: wrap;
            gap: 40px;
            opacity: 0.7;
        }

        .tech-item {
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--text-muted);
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .tech-item i {
            font-size: 1.8rem;
            color: var(--text-main);
        }

        /* --- FOOTER --- */
        .footer {
            background-color: #04060a;
            border-top: 1px solid var(--border-color);
            padding: 80px 0 30px;
        }

        .footer-grid {
            display: grid;
            grid-template-columns: 1.5fr 1fr 1fr 1.5fr;
            gap: 40px;
            margin-bottom: 60px;
        }

        .footer-brand .logo {
            margin-bottom: 20px;
        }

        .footer-brand p {
            color: var(--text-muted);
            font-size: 0.95rem;
            margin-bottom: 24px;
        }

        .footer-socials {
            display: flex;
            gap: 12px;
        }

        .footer-socials a {
            width: 36px;
            height: 36px;
            background-color: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-muted);
        }

        .footer-socials a:hover {
            color: white;
            background-color: var(--accent);
            border-color: var(--accent);
        }

        .footer-links h4 {
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 24px;
            position: relative;
        }

        .footer-links ul {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .footer-links a {
            color: var(--text-muted);
            font-size: 0.95rem;
        }

        .footer-links a:hover {
            color: var(--text-main);
            padding-left: 4px;
        }

        .footer-contact h4 {
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 24px;
        }

        .contact-info-list {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .contact-info-item {
            display: flex;
            align-items: flex-start;
            gap: 12px;
            font-size: 0.9rem;
            color: var(--text-muted);
        }

        .contact-info-item i {
            color: var(--accent);
            margin-top: 4px;
            font-size: 1.1rem;
        }

        .footer-bottom {
            border-top: 1px solid var(--border-color);
            padding-top: 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.85rem;
            color: var(--text-muted);
        }

        /* --- RESPONSIVE DESIGN --- */
        @media (max-width: 1024px) {
            .hero-grid { grid-template-columns: 1fr; gap: 40px; text-align: center; }
            .hero-content p { margin: 0 auto 36px; }
            .hero-actions { justify-content: center; }
            .hero-features { justify-content: center; }
            .stats-grid { grid-template-columns: repeat(2, 1fr); gap: 32px; }
            .stat-item { border-right: none; }
            .services-grid { grid-template-columns: repeat(2, 1fr); }
            .solutions-grid { grid-template-columns: repeat(3, 1fr); }
            .process-roadmap { grid-template-columns: 1fr; gap: 40px; }
            .process-roadmap::before { display: none; }
            .footer-grid { grid-template-columns: repeat(2, 1fr); }
        }

        @media (max-width: 768px) {
            .nav-links { display: none; }
            .hero-content h2 { font-size: 2.8rem; }
            .services-grid { grid-template-columns: 1fr; }
            .solutions-grid { grid-template-columns: repeat(2, 1fr); }
            .footer-grid { grid-template-columns: 1fr; }
            .footer-bottom { flex-direction: column; gap: 16px; text-align: center; }
        }
    </style>
</head>
<body>

    <nav class="navbar">
        <div class="container">
            <div class="logo">
                <div class="logo-box">D</div>
                <div class="logo-text">
                    <h1>DTecnología<span>YMás</span></h1>
                    <p>Innovación • Software • Infraestructura</p>
                </div>
            </div>
            <ul class="nav-links">
                <li><a href="#inicio" class="active">Inicio</a></li>
                <li><a href="#servicios">Servicios</a></li>
                <li><a href="#soluciones">Soluciones</a></li>
                <li><a href="#proceso">Proceso</a></li>
                <li><a href="#contacto">Contacto</a></li>
            </ul>
            <a href="https://wa.me/522451022162" class="btn btn-primary" target="_blank">
                <i class="fab fa-whatsapp"></i> WhatsApp
            </a>
        </div>
    </nav>

    <section class="hero" id="inicio">
        <div class="container">
            <div class="hero-grid">
                <div class="hero-content">
                    <h2>Transformamos Tecnología en <span>Soluciones Reales</span></h2>
                    <p>Desarrollamos software a la medida, aplicaciones móviles, sitios web y ofrecemos soporte técnico experto preventivo y correctivo para impulsar tu negocio al siguiente nivel.</p>
                    <div class="hero-actions">
                        <a href="https://wa.me/522451022162" class="btn btn-primary" target="_blank">Solicitar Cotización <i class="fas fa-arrow-right"></i></a>
                        <a href="#servicios" class="btn btn-secondary">Ver Servicios <i class="fas fa-play-circle"></i></a>
                    </div>
                    <div class="hero-features">
                        <div class="hero-feat-item"><i class="fas fa-certificate"></i> Personal Certificado</div>
                        <div class="hero-feat-item"><i class="fas fa-screwdriver-wrench"></i> Soporte Especializado</div>
                        <div class="hero-feat-item"><i class="fas fa-sliders"></i> Soluciones a la Medida</div>
                    </div>
                </div>
                <div class="hero-visual">
                    <div class="hero-glow-card">
                        <i class="fas fa-cubes"></i>
                        <h3 style="font-weight: 700; font-size: 1.4rem;">Ecosistema Digital 360°</h3>
                        <p style="text-align: center; font-size: 0.85rem; color: var(--text-muted); margin-top: 8px; max-width: 250px;">Hardware, conectividad y desarrollo web perfectamente sincronizados.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <div class="container">
        <div class="stats-grid">
            <div class="stat-item">
                <div class="stat-number">500<span>+</span></div>
                <div class="stat-label">Equipos atendidos</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">100<span>+</span></div>
                <div class="stat-label">Proyectos Realizados</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">10<span>+</span></div>
                <div class="stat-label">Años de experiencia</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">98<span>%</span></div>
                <div class="stat-label">Satisfacción de clientes</div>
            </div>
        </div>
    </div>

    <section class="section-padding" id="servicios">
        <div class="container">
            <div class="section-header">
                <h2>Nuestros <span>Servicios</span></h2>
                <p>Soluciones tecnológicas integrales y de vanguardia para cada necesidad de tu infraestructura o negocio.</p>
            </div>
            <div class="services-grid">
                <div class="service-card">
                    <div class="service-icon"><i class="fas fa-laptop-code"></i></div>
                    <h3>Desarrollo de Software</h3>
                    <p>Sistemas a la medida, plataformas web administrativas, software de pago o desarrollado completamente desde cero.</p>
                    <a href="https://wa.me/522451022162" class="service-link" target="_blank">Consultar <i class="fas fa-chevron-right"></i></a>
                </div>
                <div class="service-card">
                    <div class="service-icon"><i class="fas fa-mobile-alt"></i></div>
                    <h3>Aplicaciones Móviles</h3>
                    <p>Diseño y desarrollo de apps nativas e híbridas para iOS y Android adaptadas al modelo de tu empresa.</p>
                    <a href="https://wa.me/522451022162" class="service-link" target="_blank">Consultar <i class="fas fa-chevron-right"></i></a>
                </div>
                <div class="service-card">
                    <div class="service-icon"><i class="fas fa-globe"></i></div>
                    <h3>Desarrollo Web</h3>
                    <p>Diseño de páginas web de ventas (e-commerce) o landing pages corporativas de solo publicidad de alto impacto.</p>
                    <a href="https://wa.me/522451022162" class="service-link" target="_blank">Consultar <i class="fas fa-chevron-right"></i></a>
                </div>
                <div class="service-card">
                    <div class="service-icon"><i class="fas fa-network-wired"></i></div>
                    <h3>Infraestructura Tecnológica</h3>
                    <p>Instalación avanzada de conmutadores telefónicos, redes estructuradas y automatización a través de hardware.</p>
                    <a href="https://wa.me/522451022162" class="service-link" target="_blank">Consultar <i class="fas fa-chevron-right"></i></a>
                </div>
                <div class="service-card">
                    <div class="service-icon"><i class="fas fa-video"></i></div>
                    <h3>Videovigilancia Inteligente</h3>
                    <p>Instalación y configuración profesional de cámaras de videovigilancia y sistemas de monitoreo en tiempo real.</p>
                    <a href="https://wa.me/522451022162" class="service-link" target="_blank">Consultar <i class="fas fa-chevron-right"></i></a>
                </div>
                <div class="service-card">
                    <div class="service-icon"><i class="fas fa-screwdriver-wrench"></i></div>
                    <h3>Soporte Tecnológico</h3>
                    <p>Mantenimiento preventivo y correctivo de impresoras, scanners, tablets, laptops, PC y computadoras personales.</p>
                    <a href="https://wa.me/522451022162" class="service-link" target="_blank">Consultar <i class="fas fa-chevron-right"></i></a>
                </div>
            </div>
        </div>
    </section>

    <section class="section-padding solutions" id="soluciones">
        <div class="container">
            <div class="section-header">
                <h2>Soluciones <span>Para</span></h2>
                <p>Especialización técnica y metodologías adaptadas a cada tipo de sector y modelo productivo.</p>
            </div>
            <div class="solutions-grid">
                <div class="solution-card">
                    <i class="fas fa-graduation-cap"></i>
                    <h4>Educación</h4>
                    <p>Cursos particulares a diversos sectores en el ramo de TI.</p>
                </div>
                <div class="solution-card">
                    <i class="fas fa-building"></i>
                    <h4>Empresas</h4>
                    <p>Conmutadores, redes de datos y servidores corporativos.</p>
                </div>
                <div class="solution-card">
                    <i class="fas fa-shopping-cart"></i>
                    <h4>Comercios</h4>
                    <p>Páginas de ventas y automatización de servicios.</p>
                </div>
                <div class="solution-card">
                    <i class="fas fa-industry"></i>
                    <h4>Industria</h4>
                    <p>Automatización de procesos mediante software y hardware.</p>
                </div>
                <div class="solution-card">
                    <i class="fas fa-user-tie"></i>
                    <h4>Profesionales</h4>
                    <p>Soporte de cómputo de alta confiabilidad para tu día a día.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section-padding" id="proceso">
        <div class="container">
            <div class="section-header">
                <h2>Nuestro <span>Proceso</span> de Trabajo</h2>
                <p>Garantizamos resultados óptimos mediante un flujo transparente, estructurado y profesional.</p>
            </div>
            <div class="process-roadmap">
                <div class="process-step">
                    <div class="step-number">1</div>
                    <h4>Diagnóstico</h4>
                    <p>Analizamos detalladamente tu equipo o requerimiento de software.</p>
                </div>
                <div class="process-step">
                    <div class="step-number">2</div>
                    <h4>Planeación</h4>
                    <p>Diseñamos la mejor estrategia y presupuesto a la medida.</p>
                </div>
                <div class="process-step">
                    <div class="step-number">3</div>
                    <h4>Desarrollo</h4>
                    <p>Creamos, programamos o reparamos bajo estrictas normas de calidad.</p>
                </div>
                <div class="process-step">
                    <div class="step-number">4</div>
                    <h4>Implementación</h4>
                    <p>Instalamos y configuramos todo el sistema en tu entorno real.</p>
                </div>
                <div class="process-step">
                    <div class="step-number">5</div>
                    <h4>Soporte</h4>
                    <p>Te acompañamos con mantenimiento continuo y asistencia garantizada.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="tech-section">
        <div class="container">
            <div class="tech-flex">
                <div class="tech-item"><i class="fab fa-html5"></i> HTML5 & CSS3</div>
                <div class="tech-item"><i class="fab fa-js"></i> JavaScript</div>
                <div class="tech-item"><i class="fab fa-php"></i> PHP & MySQL</div>
                <div class="tech-item"><i class="fab fa-google"></i> Google Cloud</div>
                <div class="tech-item"><i class="fab fa-docker"></i> Docker Hub</div>
                <div class="tech-item"><i class="fas fa-microchip"></i> IoT / Hardware</div>
            </div>
        </div>
    </section>

    <footer class="footer" id="contacto">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <div class="logo">
                        <div class="logo-box">D</div>
                        <div class="logo-text">
                            <h1 style="color:white">DTecnología<span>YMás</span></h1>
                            <p>Transformación Digital</p>
                        </div>
                    </div>
                    <p>Brindamos soluciones tecnológicas integrales para impulsar la productividad y crecimiento de tu empresa o institución con personal certificado.</p>
                    <div class="footer-socials">
                        <a href="#"><i class="fab fa-facebook-f"></i></a>
                        <a href="#"><i class="fab fa-instagram"></i></a>
                        <a href="#"><i class="fab fa-linkedin-in"></i></a>
                    </div>
                </div>
                <div class="footer-links">
                    <h4>Enlaces</h4>
                    <ul>
                        <li><a href="#inicio">Inicio</a></li>
                        <li><a href="#servicios">Servicios</a></li>
                        <li><a href="#soluciones">Soluciones</a></li>
                        <li><a href="#proceso">Proceso</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Servicios</h4>
                    <ul>
                        <li><a href="#servicios">Desarrollo de Software</a></li>
                        <li><a href="#servicios">Aplicaciones Móviles</a></li>
                        <li><a href="#servicios">Infraestructura y Redes</a></li>
                        <li><a href="#servicios">Mantenimiento de Cómputo</a></li>
                    </ul>
                </div>
                <div class="footer-contact">
                    <h4>Contacto Directo</h4>
                    <div class="contact-info-list">
                        <div class="contact-info-item">
                            <i class="fas fa-phone-alt"></i>
                            <div>
                                <p style="font-weight: 700; color: white;">Teléfono y WhatsApp</p>
                                <p>245 102 2162</p>
                            </div>
                        </div>
                        <div class="contact-info-item">
                            <i class="fas fa-map-marker-alt"></i>
                            <div>
                                <p style="font-weight: 700; color: white;">Dirección</p>
                                <p>Manuel M. Flores 3318, Santa Cruz, Colonia 3 de mayo, 75520 Cdad. Serdán, Pue., México</p>
                            </div>
                        </div>
                        <div class="contact-info-item">
                            <i class="fas fa-clock"></i>
                            <div>
                                <p style="font-weight: 700; color: white;">Horario de Atención</p>
                                <p>9:00 AM a 9:00 PM<br>De Lunes a Sábado</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 DTecnologíaYMás. Todos los derechos reservados.</p>
                <div style="display: flex; gap: 20px;">
                    <a href="#">Política de Privacidad</a>
                    <a href="#">Términos y Condiciones</a>
                </div>
            </div>
        </div>
    </footer>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
print("File index.html generated successfully.")