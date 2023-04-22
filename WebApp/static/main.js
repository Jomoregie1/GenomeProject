
// Renders the chart using the provided data
function renderChart(data) {
    // Set chart dimensions and margins
  const margin = { top: 50, right: 30, bottom: 90, left: 80 },
    width = 460 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

   // Create the main SVG element
  const svg = d3
    .select("#chart")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);

  // Create the x-axis scale
  const x = d3
    .scaleBand()
    .range([0, width])
    .domain(data.map((d) => d.type))
    .padding(0.2);

  // Add the x-axis to the chart
  createXAxis(svg, x, height);

  // Create the y-axis scale
  const y = d3
    .scaleLinear()
    .domain([0, d3.max(data, (d) => d.count)])
    .range([height, 0]);

  // Add the y-axis to the chart
  createYAxis(svg, y, data);

  // Define the color scale
  const color = d3.scaleOrdinal()
    .domain(data.map(d => d.type))
    .range(d3.schemeCategory10);

  // Add the bars to the chart
  svg
    .selectAll("mybar")
    .data(data)
    .enter()
    .append("rect")
    .attr("x", (d) => x(d.type))
    .attr("y", (d) => y(d.count))
    .attr("width", x.bandwidth())
    .attr("height", (d) => height - y(d.count))
    .attr("fill", (d) => color(d.type));

  // Add x-axis and y-axis labels
  addAxesLabels(svg, width, height, margin);
  // Add chart title
  addTitle(svg, width, margin);
}

// Adds the x-axis to the chart
function createXAxis(svg, x, height) {
  svg
    .append("g")
    .attr("transform", `translate(0,${height})`)
    .call(d3.axisBottom(x))
    .selectAll("text")
    .style("text-anchor", "middle")
    .style("font-size", "12px");
}

// Adds the y-axis to the chart
function createYAxis(svg, y, data) {
  svg.append("g").call(d3.axisLeft(y).ticks(d3.max(data, (d) => d.count)));
}

// Adds x-axis and y-axis labels to the chart
function addAxesLabels(svg, width, height, margin) {

  // Create and position the x-axis text element
  svg.append("text")
    .attr("class", "x label")
    .attr("text-anchor", "middle")
    .attr("x", width / 2)
    .attr("y", height + margin.bottom / 1.5)
    .text("Edit Type");

  // Create and position the y-axis text element
  svg.append("text")
    .attr("class", "y label")
    .attr("text-anchor", "middle")
    .attr("y", -margin.left / 1.5)
    .attr("x", -height / 2)
    .attr("dy", ".75em")
    .attr("transform", "rotate(-90)")
    .text("Count");
}

// Adds a title to the chart
function addTitle(svg, width, margin) {

  // Create and position the title text element
  svg.append("text")
    .attr("class", "title")
    .attr("x", width / 2)
    .attr("y", -margin.top / 2)
    .attr("text-anchor", "middle")
    .style("font-size", "16px")
    .text("Distribution");
}

// Toggles the visibility of the chart based on the button click
function toggleChartVisibility(chartId, buttonId) {
  // Get the toggle button and chart elements by their IDs
  const toggleChartBtn = document.getElementById(buttonId);
  const chart = document.getElementById(chartId);

  // Add a click event listener to the toggle button
  toggleChartBtn.addEventListener("click", function () {
    // Toggle the chart display between "block" and "none"
    if (chart.style.display === "none") {
      chart.style.display = "block";
    } else {
      chart.style.display = "none";
    }
  });
}