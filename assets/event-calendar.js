(() => {
  'use strict';
  const mount = document.getElementById('calendarWidget');
  if (!mount) return;
  const market = document.getElementById('calendarMarket');
  const importance = document.getElementById('calendarImportance');
  const status = document.getElementById('calendarStatus');
  let timer;
  function render() {
    clearTimeout(timer);
    mount.replaceChildren();
    status.textContent = 'Loading scheduled events from TradingView...';
    const container = document.createElement('div');
    container.className = 'tradingview-widget-container';
    const widget = document.createElement('div');
    widget.className = 'tradingview-widget-container__widget';
    const script = document.createElement('script');
    script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-events.js';
    script.async = true;
    script.textContent = JSON.stringify({ width: '100%', height: 520, colorTheme: 'dark', isTransparent: true, locale: 'en', currencyFilter: market.value, importanceFilter: importance.value });
    script.onerror = () => { status.textContent = 'Calendar unavailable here. Open the source calendar below.'; };
    container.append(widget, script);
    mount.append(container);
    timer = setTimeout(() => { status.textContent = 'If events are not visible, open the source calendar below. Check its timezone before using a release time.'; }, 12000);
  }
  const observer = new MutationObserver(() => {
    const frame = mount.querySelector('iframe');
    if (!frame || frame.dataset.labelled) return;
    frame.dataset.labelled = 'true';
    frame.title = 'TradingView economic calendar: scheduled events';
    frame.addEventListener('load', () => {
      clearTimeout(timer);
      status.textContent = 'Source: TradingView. Times follow your device timezone; open the source calendar to check an event in detail.';
    }, { once: true });
  });
  observer.observe(mount, { childList: true, subtree: true });
  market.addEventListener('change', render);
  importance.addEventListener('change', render);
  const zone = Intl.DateTimeFormat().resolvedOptions().timeZone;
  document.getElementById('calendarLocalZone').textContent = `Event times: ${zone} (your device timezone). Daylight saving follows each event date.`;
  render();
})();
