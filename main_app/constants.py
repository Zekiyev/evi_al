
ADVERTISEMENT_TYPE_CHOICES = (
  (1, 'monthly rent'),
  (2, 'daily rent'),
  (3, 'sale'),
  (0, '##BUG##')
)

#ADVERTISEMENT_SUB_TYPE_CHOICES = (
#  (1, 'flat old constructed'),
#  (2, 'flat new constructed'),
#  (3, 'home / villa'),
#  (4, 'garden'),
#  (5, 'office'),
#  (6, 'garage'),
#  (7, 'object building'),
#  (8, 'land'),
#  (9, 'another'),
#  (0, '##BUG##'),
#
#)
#
#BUILDING_TYPE_CHOICES = (
#  (1, 'newly constructed building'),
#  (2, 'old constructed building'),
#  (3, 'business center'),
#  (4, 'other'),
#  (0, '##BUG##')
#)
#
ADVERTISEMENT_VIP_TYPE_CHOICES = (
  (1, 'normal'),
  (2, 'upper'),
  (3, 'vip'),
  (4, 'premium'),
  (0, '##BUG##')
)

BUILDING_TYPE_CHOICES = (
  (1, 'flat old constructed'),
  (2, 'flat new constructed'),
  (3, 'home / villa'),
  (4, 'garden'),
  (5, 'office'),
  (6, 'garage'),
  (7, 'object building'),
  (8, 'land'),
  (9, 'another'),
  (0, '##BUG##'),

)

ADMIN_CONFIRMATION_STATUS_CHOICES = (
  
  (1, 'initial'),
  (2, 'admin confirm'),
  (3, 'expired'),
  (4, 'other'),
  (0, '##BUG##'),

)

USER_TYPE_CHOICES = (
      (1, 'normal_seller'),
      (2, 'rieltor'),
      (3, 'agency'),
      (4, 'fake_user'),
      (5, 'another'),
      (0, '##BUG##'),
    )


BUILDING_PROJECT_TYPE_CHOICES = (
      (1, 'Xrusovka'),
      (2, 'Stalinka'),
      (3, 'Other'),
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