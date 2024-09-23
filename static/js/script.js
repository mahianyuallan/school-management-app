/*Tabs Js*/
$(function() {
  var $tabButtonItem = $('#tab-button li'),
      $tabSelect = $('#tab-select'),
      $tabContents = $('.tab-contents'),
      activeClass = 'is-active';

  $tabButtonItem.first().addClass(activeClass);
  $tabContents.not(':first').hide();

  $tabButtonItem.find('a').on('click', function(e) {
    var target = $(this).attr('href');

    $tabButtonItem.removeClass(activeClass);
    $(this).parent().addClass(activeClass);
    $tabSelect.val(target);
    $tabContents.hide();
    $(target).show();
    e.preventDefault();
  });

  $tabSelect.on('change', function() {
    var target = $(this).val(),
        targetSelectNum = $(this).prop('selectedIndex');

    $tabButtonItem.removeClass(activeClass);
    $tabButtonItem.eq(targetSelectNum).addClass(activeClass);
    $tabContents.hide();
    $(target).show();
  });
});
/*
const unitsByCourse = {
  1: [
      { id: 1, name: 'INTRO TO CS' },
      { id: 9, name: 'COMP SYS' },
      { id: 14, name: 'PROGRAMMING' }
  ],
  2: [
      { id: 8, name: 'BIOCHEM' },
      { id: 11, name: 'LABS' }
  ],
  3: [
      { id: 10, name: 'MANAGEMENT' }
  ],
  4: [
      { id: 7, name: 'SOUND SYS' },
      { id: 6, name: 'DESIGN' }
  ],
  5: [
      { id: 12, name: 'TEACHING' }
  ],
  6: [
      { id: 2, name: 'INTRO TO MECH ENG' },
      { id: 5, name: 'MECHANICS' }
  ],
  7: [
      { id: 4, name: 'A.I' },
      { id: 13, name: 'ALGEBRA' }
  ],
  8: [
      { id: 3, name: 'SURGERY' }
  ],
  24: [
      { id: 21, name: 'Into to Universe' }
  ]
};

function filterUnits() {
  const courseSelect = document.querySelector('.course-select');
  const unitSelect = document.querySelector('.unit-select');
  const selectedCourse = courseSelect.value;

  // Clear the current unit dropdown options
  unitSelect.innerHTML = '<option value="" disabled selected>Select Unit</option>';

  // Populate the unit dropdown with options related to the selected course
  if (unitsByCourse[selectedCourse]) {
      unitsByCourse[selectedCourse].forEach(unit => {
          const option = document.createElement('option');
          option.value = unit.id;
          option.text = unit.name;
          unitSelect.appendChild(option);
      });
  }
}
  */