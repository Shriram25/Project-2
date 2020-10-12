// column definitions
var columns = [
    { head: 'Movie title', cl: 'title', html: ƒ('title') },
    { head: 'Year', cl: 'center', html: ƒ('year') },
    { head: 'Length', cl: 'center', html: ƒ('length', length()) },
    { head: 'Budget', cl: 'num', html: ƒ('budget', d3.format('$,')) },
    { head: 'Rating', cl: 'num', html: ƒ('rating', d3.format('.1f')) }
];

// create table
var table = d3.select('body')
    .append('table');

// create table header
table.append('thead').append('tr')
    .selectAll('th')
    .data(columns).enter()
    .append('th')
    .attr('class', ƒ('cl'))
    .text(ƒ('head'));