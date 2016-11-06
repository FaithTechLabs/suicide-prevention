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

var getLocation = function(loc) {
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
      province = loc;
      break;
    case 'YT':
      province = 'NU';
      break;
    default:
      province = 'ON';
  }
  return province;
}

var initLocation = function(loc) {
  var province = centres[getLocation(loc)];
  $('.phone-btn').attr('href', 'tel:+' + province.phone);
  $('.number').text(formatPhone(province.phone));
  $('.name').html(province.name)
}

var initProvince = function(provinceUrl) {
  var loc = centreDictionary[provinceUrl] || 'ON';
  var province = centres[getLocation(loc)];

  $('.number').text(formatPhone(province.phone));
  $('.name').html(province.name);
  if (province.email) {
    $('.email-container').removeClass('hidden');
    $('.email').text(province.email);
    $('.email').attr('href', 'mailto:' + province.email);
  }
  if (province.address) {
    $('.address-container').removeClass('hidden');
    $('.address').text(province.address);
  }
}

var centreDictionary = {
  'Alberta': 'AB',
  'British Columbia': 'BC',
  'Manitoba': 'MB',
  'New Brunswick': 'NB',
  'Newfoundland': 'NL',
  'Nova Scotia': 'NS',
  'Northwest Territories': 'NT',
  'Nunavut': 'NU',
  'Ontario': 'ON',
  'PEI': 'PE',
  'Quebec': 'QC',
  'Saskatchewan': 'SK',
  'Yukon': 'YT'
}

var centres = {
  AB: {
    name: 'Distress Centre Calgary',
    phone: 14032264357,
    provinceName: 'Alberta',
    code: 'AB',
    email: 'info@distresscentre.com',
    address: 'Suite 300, 1010-8 Avenue SW, Calgary, AB T2P 1J2'
  },
  BC: {
    name: 'Crisis Centre of BC',
    phone: 18007842433,
    provinceName: 'British Columbia',
    code: 'BC',
    email: 'pgcrisiscentre@telus.net'
  },
  MB: {
    name: 'Reason To Live Manitoba',
    phone: 18774357170,
    provinceName: 'Manitoba',
    code: 'MB',
    email: 'klinic@klinic.mb.ca'
  },
  NB: {
    name: 'Chimo Helpline New Brunswick',
    phone: 18006675005,
    provinceName: 'New Brunswick',
    code: 'NB',
    email: 'chimo1@nb.aibn.com'
  },
  NL: {
    name: 'Mental Health Crisis Centre (NFL)',
    phone: 18887374668,
    address: '47 St  Clare Avenue, St. John’s, NF A1C 2J9'
  },
  NS: {
    name: 'Mental Health Mobile Crisis Team',
    phone: 18884298167,
    provinceName: 'Nova Scotia',
    code: 'NS'
  },
  NT: {
    name: 'NWT Help Line',
    phone: 18006610844,
    provinceName: 'Northwest Territories',
    code: 'NT',
    email: 'nwthehelpline@mail.tamarack.nt.ca'
  },
  NU: {
    name: 'Kamatsiaqtut Help Line',
    phone: 18002653333,
    provinceName: 'Nunavut',
    code: 'NU',
    email: 'slevy@qikiqtani.edu.nu.ca'
  },
  ON: {
    name: 'Mental Health Helpline Ontario',
    phone: 18665312600,
    provinceName: 'Ontario',
    code: 'ON'
  },
  PE: {
    name: 'Island Helpline',
    phone: 18002182885,
    provinceName: 'PEI',
    code: 'PEI'
  },
  QC: {
    name: 'Association québécoise de prévention du suicide',
    phone: 18662773553,
    provinceName: 'Quebec',
    code: 'QC',
    email: 'reception@aqps.info'
  },
  SK: {
    name: 'Mobile Crisis Services Saskatchewan',
    phone: 13067570127,
    provinceName: 'Saskatchewan',
    code: 'SK',
    email: 'rfield.crisissaskatoon.ca'
  }
}