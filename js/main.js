function toggleMenu() {
  document.getElementById('navLinks').classList.toggle('show');
}

function activateModule(module) {
  const moduleOutput = document.getElementById('moduleOutput');
  moduleOutput.innerText = `${module.charAt(0).toUpperCase() + module.slice(1)} module activated.`;
}

function startExperience() {
  const email = prompt("Enter your email to start:");
  if (email && email.includes('@')) {
    document.getElementById('moduleOutput').innerText = `Welcome ${email}, initializing AI interface...`;
    setTimeout(() => {
      document.getElementById('moduleOutput').innerText += "\nVisual guide and voice system activated.";
    }, 1500);
  } else {
    alert("Please enter a valid email.");
  }
}
