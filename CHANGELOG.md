# Changelog

## [0.12.0](https://github.com/linz/python-linz-logger/compare/v0.11.0...v0.12.0) (2024-04-16)


### Features

* Pin actions to hashes ([#239](https://github.com/linz/python-linz-logger/issues/239)) ([baa078d](https://github.com/linz/python-linz-logger/commit/baa078de062773caa35deb4273331a99aa13bd9c))

## 0.11.0 (2022-12-05)


### Features

* add id and hostname as default keys ([#126](https://github.com/linz/python-linz-logger/issues/126)) ([863bfac](https://github.com/linz/python-linz-logger/commit/863bfac924aa4bfbb0a4942657cc35ddcb665449))
* add trace level ([#37](https://github.com/linz/python-linz-logger/issues/37)) ([8898522](https://github.com/linz/python-linz-logger/commit/889852270dceb4c7b21c45932f68bc6103afc662))
* enable set level ([#43](https://github.com/linz/python-linz-logger/issues/43)) ([493d66d](https://github.com/linz/python-linz-logger/commit/493d66d90dcbcad8aa09192446614c1d0b35e0fc))
* initial commit of json logger ([c8300be](https://github.com/linz/python-linz-logger/commit/c8300be7b5b5ab4ff5da4653a10f3938f538e05f))
* replace threadlocal by contextvars ([#121](https://github.com/linz/python-linz-logger/issues/121)) ([4e9f16f](https://github.com/linz/python-linz-logger/commit/4e9f16f98b20671aca5a97b4a60b3bb62378179b))
* upgrade structlog version from 20.1.0 to 22.1.0 ([#120](https://github.com/linz/python-linz-logger/issues/120)) ([efb2c0f](https://github.com/linz/python-linz-logger/commit/efb2c0f32b154c89ffb9895c67afaa9661ffd4c3))


### Bug Fixes

* Allow some drift in timestamp test ([#154](https://github.com/linz/python-linz-logger/issues/154)) ([37e0416](https://github.com/linz/python-linz-logger/commit/37e04166db442640d1170dc29c3742b2a82fe253))
* Bootstrap release-please ([#159](https://github.com/linz/python-linz-logger/issues/159)) ([56b44ca](https://github.com/linz/python-linz-logger/commit/56b44ca10fbfb2807524f4c4c9adc22de8946d93))
* expose set and remove contextvars methods ([#124](https://github.com/linz/python-linz-logger/issues/124)) ([0f47982](https://github.com/linz/python-linz-logger/commit/0f47982b95e40267d61e0913745c0a0399a0b182))
* fix trace level bug ([#41](https://github.com/linz/python-linz-logger/issues/41)) ([c7e5a5a](https://github.com/linz/python-linz-logger/commit/c7e5a5a53a13f99a1761df46fc0a1bd799cc779b))
* get a timestamp not a timestamp offset by local time ([#90](https://github.com/linz/python-linz-logger/issues/90)) ([2d73ff5](https://github.com/linz/python-linz-logger/commit/2d73ff594a5b226b9d53a243146c3e34b22b911b))
* Move release-please bootstrapping configuration ([#161](https://github.com/linz/python-linz-logger/issues/161)) ([37382b1](https://github.com/linz/python-linz-logger/commit/37382b1dc6602f6ccd41a45dddb04dd67676f9ff))
* Run workflows on a specific OS version ([#151](https://github.com/linz/python-linz-logger/issues/151)) ([849cc8e](https://github.com/linz/python-linz-logger/commit/849cc8e55b593da753e965a060c7c3c9614d0353))
* Use specific action versions ([#134](https://github.com/linz/python-linz-logger/issues/134)) ([1e0e82e](https://github.com/linz/python-linz-logger/commit/1e0e82e8bff6695f3e19dcd5c363424276c492b8))


### Documentation

* correct the installation and usage documents ([#11](https://github.com/linz/python-linz-logger/issues/11)) ([064c2d9](https://github.com/linz/python-linz-logger/commit/064c2d964fcdc4bd6aee0ebb7d4eaf8c2a0d1e35))
* Tweak readme ([#75](https://github.com/linz/python-linz-logger/issues/75)) ([c5c2154](https://github.com/linz/python-linz-logger/commit/c5c2154bb78501be3f4e3f9771b28fca31b9f988))


### Continuous Integration

* force bump version ([b07cbd9](https://github.com/linz/python-linz-logger/commit/b07cbd9667caf236852ec1d6fdc39a73863d3d2f))
