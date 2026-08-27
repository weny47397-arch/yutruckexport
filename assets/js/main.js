/* ============================================
   SHACMAN Site - Main JavaScript
   ============================================ */

(function () {
    'use strict';

    // ====================
    // Mobile nav toggle
    // ====================
    const navToggle = document.querySelector('.nav-toggle');
    const mainNav = document.querySelector('.main-nav');
    if (navToggle && mainNav) {
        navToggle.addEventListener('click', () => {
            mainNav.classList.toggle('open');
            navToggle.textContent = mainNav.classList.contains('open') ? '✕' : '☰';
        });
    }

    // ====================
    // Smooth scroll for anchor links
    // ====================
    document.querySelectorAll('a[href^="#"]').forEach((a) => {
        a.addEventListener('click', (e) => {
            const id = a.getAttribute('href');
            if (id === '#' || id.length < 2) return;
            const target = document.querySelector(id);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                if (mainNav) mainNav.classList.remove('open');
            }
        });
    });

    // ====================
    // Gallery Lightbox
    // ====================
    const galleryItems = document.querySelectorAll('.gallery-item');
    let lightbox = null;

    if (galleryItems.length > 0) {
        // Create lightbox dynamically
        lightbox = document.createElement('div');
        lightbox.className = 'lightbox';
        lightbox.innerHTML = `
            <button class="lightbox-close" aria-label="Close">&times;</button>
            <img alt="" />
        `;
        document.body.appendChild(lightbox);

        const lightboxImg = lightbox.querySelector('img');
        const lightboxClose = lightbox.querySelector('.lightbox-close');

        galleryItems.forEach((item) => {
            item.addEventListener('click', () => {
                const src = item.dataset.fullsize || item.querySelector('img').src;
                lightboxImg.src = src;
                lightbox.classList.add('active');
                document.body.style.overflow = 'hidden';
            });
        });

        const closeLightbox = () => {
            lightbox.classList.remove('active');
            document.body.style.overflow = '';
        };

        lightbox.addEventListener('click', closeLightbox);
        lightboxClose.addEventListener('click', (e) => {
            e.stopPropagation();
            closeLightbox();
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && lightbox.classList.contains('active')) {
                closeLightbox();
            }
        });
    }

    // ====================
    // Contact Form
    // ====================
    // (提交处理在 contact.html 内嵌, 不在主 JS 里)

    // ====================
    // Reveal on scroll (simple version)
    // ====================
    const reveal = document.querySelectorAll('.section .section-head, .series-card, .feature-item, .stat-item');

    if ('IntersectionObserver' in window && reveal.length > 0) {
        const obs = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                        obs.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.15 }
        );

        reveal.forEach((el) => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            obs.observe(el);
        });
    }
})();
