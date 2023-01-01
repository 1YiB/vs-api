unofficial api wrapper for open-vsx & vs-marketplace

- info api stable on openvsx

### TODO

>  [`@open-vsx`](https://open-vsx.org)

- [x] basic json httpx api request
- [x] custom types for input of arguments
- [ ] custom json mapping models - (remaining:,`reviews`,`publisher`)
- [ ] map json using models , write unit tests , add docstrings (remaining:,,`reviews`,`publisher`)


> [`@vs-marketplace`](https://marketplace.visualstudio.com)

- [ ] not started


## Refference for reverse-engineering:

marketplace

- https://visualstudio.marketplace.com (Network devtools)

open-vsx
- https://github.com/eclipse/openvsx/blob/master/webui/src/pages/extension-list/extension-list-container.tsx (source code: java-spring & react)
