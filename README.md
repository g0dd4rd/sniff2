# sniff2
sniff2 can be used for:
- inspecting UI components and widgets on GNOME desktop
- generating a behave-like (BDD) directory structure
- writing GUI tests together with dogtail framework

# 'Installation'
- make sure you have installed dogtail
- put sniff2 and queryEditWindow into /usr/bin/ or wherever else

# Behavior
- currently, the queryEditorWindow writes Behave steps definitions (the actual Python def stubs) into ~/dogtail-behave-projects/example-app/features/steps/steps.py if no app is specified
- queryEditorWindow currently *overwrites* the steps.py file

