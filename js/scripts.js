// Modul klik hadisələri üçün
document.addEventListener("DOMContentLoaded", () => {
  const modules = document.querySelectorAll(".module-btn");

  modules.forEach((btn) => {
    btn.addEventListener("click", () => {
      const moduleName = btn.getAttribute("data-module");
      activateModule(moduleName);
    });
  });
});

function activateModule(name) {
  const statusBox = document.getElementById("statusBox");
  statusBox.innerText = `Modul aktivdir: ${name}`;
  
  // Süni intellektlə sinxron (placeholder funksiyalar)
  speak(`Activated ${name} module.`);
  visualGuide(name);
}

function speak(text) {
  if ('speechSynthesis' in window) {
    const msg = new SpeechSynthesisUtterance(text);
    msg.lang = "en-US";
    window.speechSynthesis.speak(msg);
  }
}

function visualGuide(name) {
  // Göstərişlər üçün sadə vizual təlimat
  const guide = document.getElementById("visualGuide");
  guide.innerText = `You are now in the ${name} module.`;
}
