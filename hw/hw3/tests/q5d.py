test = {
  'name': 'q5d',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> tidy_format.loc[894661651760377856].shape
          (27, 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ' '.join(list(tidy_format.loc[894661651760377856]['word']))
          'i think senator blumenthal should take a nice long vacation in vietnam where he lied about his service so he can at least say he was there'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
