{
  'targets': [
    {
      'target_name': 'bindings',
      'sources': [
        'src/LocationManager.mm',
        'src/CLLocationBindings.mm'
      ],
      "xcode_settings": {
        "OTHER_CFLAGS": [
          "-std=c++20"
        ]
      },
      "cflags_cc": [
        "-std=c++20"
      ],
      'link_settings': {
        'libraries': [
          'CoreLocation.framework'
        ]
      }
    }
  ]
}
