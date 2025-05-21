const translations = {
  az: {
    title: "Al Eye – Ağıllı Yoldaşınız",
    headline: "Al Eye – Gələcəyin Ağıllı Yoldaşı",
    modules: "Modullar",
    contact: "Əlaqə",
    start: "Başla"
  },
  en: {
    title: "Al Eye – Your Smart Companion",
    headline: "Al Eye – The Smart Assistant of the Future",
    modules: "Modules",
    contact: "Contact",
    start: "Start"
  },
  tr: {
    title: "Al Eye – Akıllı Yardımcınız",
    headline: "Al Eye – Geleceğin Akıllı Yol Arkadaşı",
    modules: "Modüller",
    contact: "İletişim",
    start: "Başlat"
  }
};

function detectLanguage() {
  const lang = navigator.language.slice(0, 2);
  return translations[lang] ? lang : "az";
}

function applyTranslations() {
  const lang = detectLanguage();
  const t = translations[lang];
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.getAttribute("data-i18n");
    if (t[key]) el.innerText = t[key];
  });
}

function startExperience() {
  const email = prompt("E-poçtunuzu daxil edin:");
  if (email) {
    const msg = new SpeechSynthesisUtterance("Salam, xoş gəlmisiniz!");
    window.speechSynthesis.speak(msg);
    alert("Vizual bələdçi aktiv edildi.");
  }
}

document.addEventListener("DOMContentLoaded", applyTranslations);
