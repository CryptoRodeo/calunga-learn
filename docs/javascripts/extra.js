document$.subscribe(function() {
  mermaid.initialize({
    startOnLoad: true,
    theme: "dark",
    themeVariables: {
      primaryColor: "#1a237e",
      primaryTextColor: "#fff",
      primaryBorderColor: "#ee0000",
      lineColor: "#ee0000",
      secondaryColor: "#004d40",
      tertiaryColor: "#1a1a2e",
      fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif",
      fontSize: "14px"
    },
    flowchart: { curve: "basis", padding: 10 },
    sequence: { mirrorActors: false }
  });
});
