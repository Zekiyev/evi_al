
ADVERTISEMENT_TYPE_CHOICES = (
  (1, 'Kirayə'),
  (2, 'Günlük kirayə'),
  (3, 'Satış'),
  (4, 'Başqa')
)

ADVERTISEMENT_SUB_TYPE_CHOICES = (
  (1, 'sub_flat old constructed'),
  (2, 'sub_flat new constructed'),
  (3, 'sub_home / villa'),
  (4, 'sub_garden'),
  (5, 'sub_office'),
  (6, 'sub_garage'),
  (7, 'sub_object building'),
  (8, 'sub_land'),
  (9, 'sub_another'),

)


ADVERTISEMENT_VIP_TYPE_CHOICES = (
  (1, 'Normal'),
  (2, 'Önə çəkilmiş'),
  (3, 'Vip'),
  (4, 'Premium'),
  (5, 'Başqa')
)

BUILDING_TYPE_CHOICES = (
  (1, 'Köhnə tikili'),
  (2, 'Yeni tikili'),
  (3, 'Ev / villa'),
  (4, 'Bağ'),
  (5, 'Ofis'),
  (6, 'Qaraj'),
  (7, 'Obyekt'),
  (8, 'Torpaq'),
  (9, 'Başqa'),

)

ADMIN_CONFIRMATION_STATUS_CHOICES = (
  
  (1, 'Gözləmədədir'),
  (2, 'Təsdiqlənib'),
  (3, 'Vaxtı bitmişdir'),
  (4, 'Başqa'),


)

USER_TYPE_CHOICES = (
      (1, 'normal_seller'),
      (2, 'rieltor'),
      (3, 'agency'),
      (4, 'fake_user'),
      (5, 'another'),
    )


BUILDING_PROJECT_TYPE_CHOICES = (
      (1, 'Xruşovka'),
      (2, 'Stalinka'),
      (3, 'Başqa'),
    )

PAYMENT_STATUS_CHOICES = (
      (1, 'Pending Payment'),
      (2, 'Transfer Success'),
      (3, 'Transfer Failed'),
    )

TRANSACTION_OPERATION_CHOICES = (
      (1, 'Debet'),
      (2, 'Credit'),
    )