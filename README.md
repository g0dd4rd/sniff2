# sniff2
sniff2 can be used for:
- inspecting UI components and widgets on GNOME desktop
- generating a behave-like (BDD) directory structure
- writing GUI tests together with dogtail framework

# 'Installation'
- make sure you have installed dogtail and behave
- put sniff2 and queryEditWindow into /usr/bin/ or wherever else

# Behavior
- currently, the queryEditorWindow writes:
-- dogtail queries (the actual Python def stubs) into ~/dogtail-behave-projects/${app}/features/steps/steps.py or to example-app if no app is specified
-- behave steps (the actual scenarios for given test(s)) into ~/dogtail-behave-projects/${app}/features/general.feature
-- queryEditorWindow currently *overwrites* the general.feature and steps.py files

