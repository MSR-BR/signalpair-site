(() => {
  const body = document.body;
  const buttons = [...document.querySelectorAll("[data-set-language]")];
  const preferred = new URLSearchParams(location.search).get("lang");
  const initial = preferred === "pt" ? "pt" : "en";

  function setLanguage(language) {
    body.dataset.language = language;
    document.documentElement.lang = language === "pt" ? "pt-BR" : "en";
    buttons.forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.setLanguage === language));
    });
    document.querySelectorAll("a[href]").forEach((link) => {
      const href = link.getAttribute("href");
      if (!href || href.startsWith("#") || href.startsWith("http") || href.startsWith("mailto:")) return;
      const [path, hash = ""] = href.split("#");
      const target = new URL(path, location.href);
      target.searchParams.set("lang", language);
      link.setAttribute("href", target.pathname.split("/").pop() + target.search + (hash ? "#" + hash : ""));
    });
  }

  buttons.forEach((button) => button.addEventListener("click", () => setLanguage(button.dataset.setLanguage)));
  setLanguage(initial);

  const local = location.protocol === "file:" || ["localhost", "127.0.0.1"].includes(location.hostname);
  document.querySelectorAll("[data-local-preview]").forEach((item) => { item.hidden = !local; });
})();
