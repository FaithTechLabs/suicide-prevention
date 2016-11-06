$(document).foundation()

var navClick = function() {
  $('.nav ul').toggleClass('hide-for-small-only');
}

var formatPhone = function(num) {
  num = num.toString();
  var phone = num[0];
  phone += ' (' + num.slice(1, 4) + ') ';
  phone += num.slice(4, 7) + '-' + num.slice(7);
  return phone;
}

var initLocation = function(loc) {
  var province;
  switch(loc) {
    case 'AB':
    case 'BC':
    case 'MB':
    case 'NB':
    case 'NL':
    case 'NS':
    case 'NT':
    case 'ON':
    case 'PE':
    case 'QC':
    case 'SK':
    case 'NU':
      obj = loc;
      break;
    case 'YT':
      // 24/7 service for Nunavut
      obj = 'NU';
      break;
    default:
      // Ontario number
      obj = 'ON';
  }

  var province = centres[obj];
  $('.phone-btn').attr('href', 'tel:+' + province.phone);
  $('.phone-btn .number').text(formatPhone(province.phone));
  $('.phone-btn .name').html(province.name)
}

var centres = {
  AB: {
    name: 'Distress Centre Calgary',
    phone: 14032264357
  },
  BC: {
    name: 'Crisis Centre of BC',
    phone: 18007842433
  },
  MB: {
    name: 'Reason To Live Manitoba',
    phone: 18774357170
  },
  NB: {
    name: 'Chimo Helpline New Brunswick',
    phone: 18006675005
  },
  NT: {
    name: 'NWT Help Line',
    phone: 18006610844
  },
  NU: {
    name: 'Kamatsiaqtut Help Line',
    phone: 18002653333
  },
  ON: {
    name: 'Mental Health Helpline Ontario',
    phone: 18665312600
  },
  QC: {
    name: 'Association québécoise de prévention du suicide',
    phone: 18662773553
  },
  SK: {
    name: 'Mobile Crisis Services Saskatchewan',
    phone: 13067570127
  }
}