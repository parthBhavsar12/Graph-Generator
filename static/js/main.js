let serialNumber = 2;

document.getElementById('add-row').addEventListener('click', function () {
    const tableBody = document.querySelector('tbody');

    const newRow = document.createElement('tr');

    const serialCell = document.createElement('th');
    serialCell.setAttribute('scope', 'row');
    serialCell.textContent = serialNumber++;

    const xCell = document.createElement('td');
    const xInput = document.createElement('input');
    xInput.setAttribute('type', 'text');
    xInput.setAttribute('placeholder', 'Enter Data for X-Axis');
    xInput.setAttribute('id', `data_x_axis_${serialNumber}`);
    xInput.setAttribute('name', `data_x_axis_${serialNumber}`);
    xInput.setAttribute('required', `true`);
    xCell.appendChild(xInput);

    const yCell = document.createElement('td');
    const yInput = document.createElement('input');
    yInput.setAttribute('type', 'text');
    yInput.setAttribute('placeholder', 'Enter Data for Y-Axis');
    yInput.setAttribute('id', `data_y_axis_${serialNumber}`);
    yInput.setAttribute('name', `data_y_axis_${serialNumber}`);
    yInput.setAttribute('required', `true`);
    yCell.appendChild(yInput);

    newRow.appendChild(serialCell);
    newRow.appendChild(xCell);
    newRow.appendChild(yCell);

    tableBody.appendChild(newRow);
});

msg = document.getElementById('msg');
setTimeout(() => {
    msg.style.display = "none";
  }, "2500");