window.onload = function () {
  const fileInput = document.getElementById("id_image");
  const fileName = document.getElementById("file-name");

  fileInput.addEventListener("change", () => {
    fileName.textContent =
      fileInput.files.length > 0 ? fileInput.files[0].name : "No file chosen";
  });
};
