// Theme Toggle
(function() {
  const THEME_KEY = 'prompt2production-theme';
  const LIGHT = 'light';
  const DARK = 'dark';

  function getSystemTheme() {
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      return DARK;
    }
    return LIGHT;
  }

  function getSavedTheme() {
    return localStorage.getItem(THEME_KEY);
  }

  function getTheme() {
    const saved = getSavedTheme();
    if (saved) return saved;
    return getSystemTheme();
  }

  function applyTheme(theme) {
    const isDark = theme === DARK;
    document.documentElement.setAttribute('data-theme', theme);
    document.body.setAttribute('data-theme', theme);
    localStorage.setItem(THEME_KEY, theme);
    
    // Update button
    const btn = document.getElementById('theme-toggle-btn');
    if (btn) {
      btn.textContent = isDark ? '☀️' : '🌙';
      btn.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
    }
  }

  function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme') || getTheme();
    const newTheme = current === DARK ? LIGHT : DARK;
    applyTheme(newTheme);
  }

  // Initialize
  document.addEventListener('DOMContentLoaded', function() {
    const theme = getTheme();
    applyTheme(theme);

    // Add toggle button
    const btn = document.getElementById('theme-toggle-btn');
    if (btn) {
      btn.addEventListener('click', toggleTheme);
    }
  });

  // Listen to system theme changes
  if (window.matchMedia) {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
      if (!getSavedTheme()) {
        applyTheme(e.matches ? DARK : LIGHT);
      }
    });
  }

  // Expose toggle function globally
  window.toggleTheme = toggleTheme;
})();
