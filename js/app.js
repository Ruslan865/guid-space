function startExperience() {
  const email = prompt("E-poçtunuzu daxil edin:");
  if (email) {
    const msg = new SpeechSynthesisUtterance("Salam, xoş gəlmisiniz!");
    window.speechSynthesis.speak(msg);
    alert("Vizual bələdçi aktiv edildi.");
  }
}
