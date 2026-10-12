function copyText(text) {
  // execCommand works in extension pages with clipboardWrite, even before the
  // popup gains focus (navigator.clipboard.writeText throws "Document is not focused").
  const ta = document.createElement("textarea");
  ta.value = text;
  document.body.appendChild(ta);
  ta.select();
  const ok = document.execCommand("copy");
  ta.remove();
  if (!ok) throw new Error("copy command was rejected");
}

(async () => {
  const status = document.getElementById("status");
  try {
    const tabs = await chrome.tabs.query({ highlighted: true, currentWindow: true });
    const urls = tabs.map((t) => t.url || t.pendingUrl).filter(Boolean);
    copyText(urls.join("\n"));
    status.textContent = `Copied ${urls.length} URL${urls.length === 1 ? "" : "s"}`;
    setTimeout(() => window.close(), 900);
  } catch (err) {
    status.textContent = `Failed: ${err.message}`;
  }
})();
