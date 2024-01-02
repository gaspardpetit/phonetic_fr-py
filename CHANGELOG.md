### 2024-01-02

- Added special handling of `ver` which was converted as `VE` while `VERS` and `verre` were converted to `VER`. `ver` is now a special case and converts to `VER`

- Handling of accents moved to a later stage so that their impact is considered. For example `poésie` would be first converted to `POESIE` and then `POSI` instead of `POESI`. There are still issues with accents, for example `ténuité` is converted to `TENUITE` and then `EN` is still converted to `AN` resulting in `TANUIT`. [https://github.com/gaspardpetit/phonetic_fr-py/issues/4]

- Special case was added for `DILEM` and `DILLEM` since double `LL` are simplified to single `L` and `DILEM` was then assumed convert to `DIEM` instead of `DILEM`. `dilemme` now converts to `DILEM`.

- Special handling of `ver` was added - words ending in `ER` are stripped unless very short, and `ver` would be converted to `VE`, which does not compare well to `verre` or `vers` which both convert to `VER`. `ver` now converts to `VER`

### 2024-01-01

Original version ported from https://github.com/EdouardBERGE/phonetic

authored by 
- Édouard Bergé

crediting:
- Frédéric Brouard
- Florent Bruneau
- Christophe Pythoud et Vazkor (Jean-Claude M.)