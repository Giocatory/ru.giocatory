// Переключение глав
function toggleChapter(chapterNum) {
    const chapter = document.querySelector(
      `[data-chapter="${chapterNum}"]`
    );
    const content = chapter.querySelector(".chapter-content");
    const arrow = chapter.querySelector("span");

    content.style.display =
      content.style.display === "block" ? "none" : "block";
    arrow.textContent = content.style.display === "block" ? "▲" : "▼";
  }

  // Показать контент
  function showContent(contentId) {
    document.querySelectorAll(".content-block").forEach((el) => {
      el.classList.remove("active-content");
    });
    document.getElementById(contentId).classList.add("active-content");
  }

  // По умолчанию открываем первый контент
  window.onload = () => showContent("intro-1");