(() => {
  const body = document.body;
  const storageKey = "signalpair-language";
  const buttons = [...document.querySelectorAll("[data-set-language]")];
  const preferred = new URLSearchParams(location.search).get("lang");
  const stored = localStorage.getItem(storageKey);
  const initial = preferred === "pt" || preferred === "en" ? preferred : stored === "pt" ? "pt" : "en";

  function updateActiveNavigation() {
    const page = location.pathname.split("/").pop() || "index.html";
    const active = page === "methodology.html" ? "method" : page === "index.html" && location.hash !== "#episodes" ? "home" : "episodes";
    document.querySelectorAll("[data-global-nav] a").forEach((link) => {
      if (link.dataset.nav === active) link.setAttribute("aria-current", "page");
      else link.removeAttribute("aria-current");
    });
  }

  function setLanguage(language) {
    body.dataset.language = language;
    document.documentElement.lang = language === "pt" ? "pt-BR" : "en";
    localStorage.setItem(storageKey, language);
    buttons.forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.setLanguage === language));
    });
    document.querySelectorAll("a[href]").forEach((link) => {
      const href = link.getAttribute("href");
      if (!href || href.startsWith("#") || href.startsWith("http") || href.startsWith("mailto:") || link.hasAttribute("download") || link.hasAttribute("data-preserve-href")) return;
      const [path, hash = ""] = href.split("#");
      const target = new URL(path, location.href);
      target.searchParams.set("lang", language);
      link.setAttribute("href", target.pathname.split("/").pop() + target.search + (hash ? "#" + hash : ""));
    });
    updateActiveNavigation();
  }

  buttons.forEach((button) => button.addEventListener("click", () => setLanguage(button.dataset.setLanguage)));
  setLanguage(initial);
  addEventListener("hashchange", updateActiveNavigation);

  const local = location.protocol === "file:" || ["localhost", "127.0.0.1"].includes(location.hostname);
  document.querySelectorAll("[data-local-preview]").forEach((item) => { item.hidden = !local; });
})();
