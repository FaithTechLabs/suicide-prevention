$(document).foundation()

var initLocation = function(loc) {
  var phone;
  switch(loc) {
    case 'AB':
      phone = '+14032264357';
      break;
    case 'BC':
      phone = '+18007842433';
      break;
    case 'MB':
      phone = '+18774357170';
      break;
    case 'NB':
      phone = '+18006675005';
      break;
    case 'NL':
      phone = '+18887374668';
      break;
    case 'NS':
      phone = '+18884298167';
      break;
    case 'NT':
      // 7-11pm (?) resource
      phone = '+18006610844';
      break;
    case 'PE':
      phone = '+18002182885';
      break;
    case 'QC':
      phone = '+18662773553';
      break;
    case 'SK':
      phone = '+13067570127';
      break;
    case 'NU':
    case 'YT':
      // 24/7 service for Nunavut
      phone = '+18002653333';
      break;
    default:
      // Ontario number
      phone = '+18665312600';
      break;
  }

  $('#phoneButton').attr('href', 'tel:' + phone);
}
