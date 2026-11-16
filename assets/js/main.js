/* Custom Made Canvas Canopies: nav state, menu, reveals, gallery filter + lightbox, shade rail, WhatsApp quote form. */
(() => {
  const doc = document.documentElement;
  doc.classList.add("js");
  const WA = "27829508390";
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();

  /* Nav background + mobile dock: watch the hero instead of listening to scroll */
  const nav = document.querySelector(".nav");
  const hero = document.querySelector(".hero");
  const dock = document.querySelector(".dock");
  if (nav && hero && "IntersectionObserver" in window) {
    new IntersectionObserver(([e]) => {
      const past = !e.isIntersecting;
      nav.dataset.state = past ? "scrolled" : "top";
      if (dock) dock.classList.toggle("is-shown", past);
    }, { rootMargin: "-72px 0px 0px 0px", threshold: 0.02 }).observe(hero.querySelector(".hero__title") || hero);
  } else if (nav) {
    nav.dataset.state = "scrolled";
  }

  /* Mobile menu */
  const toggle = document.querySelector(".nav__toggle");
  const menu = document.getElementById("menu");
  const setMenu = (open) => {
    if (!menu) return;
    menu.hidden = !open;
    nav.classList.toggle("is-open", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    document.body.style.overflow = open ? "hidden" : "";
  };
  if (toggle) {
    toggle.addEventListener("click", () => setMenu(menu.hidden));
    menu.addEventListener("click", (e) => { if (e.target.closest("a")) setMenu(false); });
    addEventListener("keydown", (e) => { if (e.key === "Escape" && !menu.hidden) setMenu(false); });
    matchMedia("(min-width: 1021px)").addEventListener("change", (m) => { if (m.matches) setMenu(false); });
  }

  /* Scroll reveals with a small stagger inside each parent */
  const reveals = document.querySelectorAll(".reveal");
  if (!reduce && "IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        const sibs = [...e.target.parentElement.querySelectorAll(":scope > .reveal")];
        e.target.style.setProperty("--d", `${Math.min(sibs.indexOf(e.target), 5) * 70}ms`);
        e.target.classList.add("in");
        io.unobserve(e.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
    reveals.forEach((el) => io.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add("in"));
  }

  /* Gallery filter */
  const shots = [...document.querySelectorAll(".shot")];
  const chips = document.querySelectorAll(".chip");
  chips.forEach((chip) => chip.addEventListener("click", () => {
    const f = chip.dataset.filter;
    chips.forEach((c) => c.setAttribute("aria-pressed", String(c === chip)));
    shots.forEach((s) => { s.hidden = f !== "all" && s.dataset.cat !== f; });
  }));

  /* Lightbox */
  const lb = document.getElementById("lightbox");
  const lbImg = document.getElementById("lb-img");
  const lbCap = document.getElementById("lb-cap");
  let idx = 0;
  const visible = () => shots.filter((s) => !s.hidden);
  const show = (i) => {
    const list = visible();
    idx = (i + list.length) % list.length;
    const a = list[idx];
    const alt = a.querySelector("img").alt;
    lbImg.src = a.getAttribute("href");
    lbImg.alt = alt;
    lbCap.textContent = alt;
  };
  if (lb && typeof lb.showModal === "function") {
    shots.forEach((a) => a.addEventListener("click", (e) => {
      e.preventDefault();
      show(visible().indexOf(a));
      lb.showModal();
      document.body.style.overflow = "hidden";
    }));
    lb.addEventListener("close", () => { document.body.style.overflow = ""; lbImg.removeAttribute("src"); });
    lb.addEventListener("click", (e) => {
      const act = e.target.closest("[data-lb]")?.dataset.lb;
      if (act === "close" || e.target === lb || e.target.tagName === "FIGURE") lb.close();
      if (act === "prev") show(idx - 1);
      if (act === "next") show(idx + 1);
    });
    lb.addEventListener("keydown", (e) => {
      if (e.key === "ArrowLeft") show(idx - 1);
      if (e.key === "ArrowRight") show(idx + 1);
    });
    let x0 = null;
    lb.addEventListener("touchstart", (e) => { x0 = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener("touchend", (e) => {
      if (x0 === null) return;
      const dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 50) show(idx + (dx < 0 ? 1 : -1));
      x0 = null;
    });
  }

  /* Shade rail buttons */
  const rail = document.getElementById("shade-rail");
  document.querySelectorAll("[data-scroll]").forEach((b) => b.addEventListener("click", () => {
    const step = rail.querySelector(".slide").getBoundingClientRect().width + 16;
    rail.scrollBy({ left: step * Number(b.dataset.scroll), behavior: reduce ? "auto" : "smooth" });
  }));

  /* Quote form opens WhatsApp with a ready message */
  const form = document.getElementById("quote");
  if (form) {
    const name = form.elements.name;
    const err = document.getElementById("q-name-err");
    name.addEventListener("input", () => { if (name.value.trim()) { err.hidden = true; name.removeAttribute("aria-invalid"); } });
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!name.value.trim()) {
        err.hidden = false;
        name.setAttribute("aria-invalid", "true");
        name.setAttribute("aria-describedby", "q-name-err");
        name.focus();
        return;
      }
      const needs = [...form.querySelectorAll('input[name="need"]:checked')].map((i) => i.value);
      const lines = [`Hi Neels, my name is ${name.value.trim()}.`];
      if (form.elements.vehicle.value.trim()) lines.push(`Vehicle: ${form.elements.vehicle.value.trim()}`);
      if (needs.length) lines.push(`Interested in: ${needs.join(", ")}`);
      if (form.elements.message.value.trim()) lines.push(form.elements.message.value.trim());
      lines.push("(Sent from your website)");
      window.open(`https://wa.me/${WA}?text=${encodeURIComponent(lines.join("\n"))}`, "_blank", "noopener");
    });
  }
})();
