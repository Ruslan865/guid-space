<!DOCTYPE html>
<html lang="az">
<head>
  <meta charset="UTF-8">
  <title>Al Eye – Master Sinxron Panel</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-900 text-white font-sans">

  <div class="max-w-5xl mx-auto p-6">
    <!-- Başlıq -->
    <h1 class="text-4xl font-bold text-center text-cyan-400 mb-8">🧠 Al Eye – Birləşmiş Modul İdarə Sistemi</h1>

    <!-- Modul Seçimi -->
    <div class="grid grid-cols-2 md:grid-cols-3 gap-4 mb-8">
      <button onclick="activateModule('idmanci')" class="btn">🏋️‍♂️ İdmançı</button>
      <button onclick="activateModule('psixoloq')" class="btn">🧘 Psixoloq</button>
      <button onclick="activateModule('yasli')" class="btn">👵 Yaşlılara dəstək</button>
      <button onclick="activateModule('usaq')" class="btn">👶 Uşaq və Ailə</button>
      <button onclick="activateModule('avto')" class="btn">🚗 Avtomobil</button>
      <button onclick="activateModule('muellim')" class="btn">📚 Müəllim</button>
      <button onclick="activateModule('hekim')" class="btn">🩺 Həkim</button>
      <button onclick="activateModule('moda')" class="btn">👗 Moda / Alış-veriş</button>
      <button onclick="activateModule('internet')" class="btn">🌐 İnternet / AI Sorğu</button>
    </div>

    <!-- Aktiv Modul Vizualı və Səsi -->
    <div id="moduleOutput" class="p-6 rounded-lg bg-gray-800 shadow-lg text-center">
      <h2 class="text-2xl text-yellow-300 font-bold mb-4">Modul aktiv deyil...</h2>
      <p class="text-lg text-gray-200">Yuxarıdakı modullardan birini seçin.</p>
    </div>
  </div>

  <style>
    .btn {
      background-color: #2d3748;
      padding: 12px;
      border-radius: 10px;
      text-align: center;
      font-weight: bold;
      transition: 0.3s;
    }
    .btn:hover {
      background-color: #4fd1c5;
      color: black;
    }
  </style>

  <script>
    const moduleData = {
      idmanci: {
        title: "🏋️‍♂️ İdmançı Modulu Aktivdir",
        text: "Fiziki aktivliyin analizini aparıram. Hazırsan, başlayaq!",
        voice: "İdman zamanı bədən vəziyyətini analiz edirəm. Gəlin məşqə başlayaq!"
      },
      psixoloq: {
        title: "🧘 Psixoloq Modulu Aktivdir",
        text: "Səni dinləyirəm... Əhvalın necədir?",
        voice: "Mən buradayam. Əhvalınla bağlı danışa bilərik."
      },
      yasli: {
        title: "👵 Yaşlılara Dəstək Modulu Aktivdir",
        text: "Sevdiyiniz səs ilə sizə qayğı göstərirəm.",
        voice: "Gözəl günlər sizinlə olsun. Nə etməyimi istəyirsiniz?"
      },
      usaq: {
        title: "👶 Uşaq və Ailə Modulu Aktivdir",
        text: "Gəlin bir az əylənək və öyrənək!",
        voice: "Salam balaca dostum! Bu gün hansı oyunla başlayaq?"
      },
      avto: {
        title: "🚗 Avtomobil Təhlükəsizlik Modulu Aktivdir",
        text: "Yol hərəkətini analiz edirəm. Təhlükəsiz sür!",
        voice: "Sükan arxasındasan. Diqqətli ol, mən səni izləyirəm."
      },
      muellim: {
        title: "📚 Müəllim Modulu Aktivdir",
        text: "Bugünkü dərsimiz üçün hazıram!",
        voice: "Gəlin birlikdə öyrənək. Hər sualın cavabı var."
      },
      hekim: {
        title: "🩺 Həkim Modulu Aktivdir",
        text: "Sağlamlığınız vacibdir. Nə hiss edirsiniz?",
        voice: "Zəhmət olmasa, simptomlarınızı izah edin."
      },
      moda: {
        title: "👗 Moda və Alış-veriş Modulu Aktivdir",
        text: "Bu gün hansı stildə geyinmək istəyirsiniz?",
        voice: "Stilinizi qiymətləndirirəm. Gəlin uyğun paltar seçək."
      },
      internet: {
        title: "🌐 İnternet və Süni Zəka Sorğusu Aktivdir",
        text: "Nə öyrənmək istəyirsiniz? Axtarışa hazıram!",
        voice: "Sualınızı söyləyin, mən internetdə cavab tapım."
      }
    };

    function activateModule(key) {
      const data = moduleData[key];
      const out = document.getElementById("moduleOutput");
      out.innerHTML = `
        <h2 class="text-2xl text-green-300 font-bold mb-4">${data.title}</h2>
        <p class="text-lg text-white">${data.text}</p>
      `;
      speak(data.voice);
    }

    function speak(text) {
      const synth = window.speechSynthesis;
      const utter = new SpeechSynthesisUtterance(text);
      utter.lang = "az-AZ";
      synth.cancel(); // digərlərini dayandır
      synth.speak(utter);
    }
  </script>
</body>
</html>
