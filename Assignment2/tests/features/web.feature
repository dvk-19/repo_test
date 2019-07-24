@web @google

  Feature: I want to download firefox

    Scenario: When I search google, to download firefox
      Given Google Search Engine
      When I enter Firefox
      Then Results for Firefox are found
