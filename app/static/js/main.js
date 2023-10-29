document.addEventListener("DOMContentLoaded", function () {
  const images = document.querySelectorAll(".img-thumbnail");
  let currentImageIndex = 0;

  const prevButton = document.getElementById("prev");
  const nextButton = document.getElementById("next");

  function showImage(index) {
    if (index < 0) {
      index = 0; // No retroceder más allá del primer elemento
    } else if (index >= images.length) {
      index = images.length - 1; // No avanzar más allá del último elemento
    }

    images.forEach((image, i) => {
      if (i === index) {
        image.style.display = "block";
      } else {
        image.style.display = "none";
      }
    });

    currentImageIndex = index;

    // Deshabilitar botón "Anterior" cuando estamos en el primer elemento
    prevButton.disabled = currentImageIndex === 0;

    // Deshabilitar botón "Siguiente" cuando estamos en el último elemento
    nextButton.disabled = currentImageIndex === images.length - 1;
  }

  // Mostrar la primera imagen al cargar la página
  showImage(0);

  prevButton.addEventListener("click", function () {
    showImage(currentImageIndex - 1);
  });

  nextButton.addEventListener("click", function () {
    showImage(currentImageIndex + 1);
  });
});
