<p align="center">
  <a href="https://gamemaker.io/en/showcase/climb-a-mountain-in-your-pocket">
    <img src="https://assets.gamemaker.io/climb_a_mountain_in_your_pocket_vid_climb_fda2281d28.jpg" alt="Climb! A Mountain in Your Pocket" width="760">
  </a>
</p>

<h1 align="center">Climb! A Mountain in Your Pocket — PortMaster</h1>

<p align="center">
  <img alt="Plataforma" src="https://img.shields.io/badge/plataforma-PortMaster-2ea44f">
  <img alt="Arquitetura" src="https://img.shields.io/badge/arquitetura-ARM-blue">
  <img alt="Engine" src="https://img.shields.io/badge/engine-GameMaker-orange">
  <img alt="Licença" src="https://img.shields.io/badge/licença-MIT-yellow">
</p>

<p align="center">
  <a href="#portugues"><img src="https://img.shields.io/badge/🇧🇷_PORTUGUÊS-2ea44f?style=for-the-badge" alt="Português"></a>
  <a href="#english"><img src="https://img.shields.io/badge/🇺🇸_ENGLISH-0969da?style=for-the-badge" alt="English"></a>
</p>

<a id="portugues"></a>

# 🇧🇷 Português

Um port não oficial para PortMaster da versão Android de **Climb! A Mountain in Your Pocket**. O runtime do GameMaker é executado no Linux através do **GMLoader**, permitindo jogar em portáteis ARM compatíveis, como o **R36S**.

> **BYO-data:** este repositório não inclui o jogo, APK, XAPK, assets protegidos nem qualquer outro dado proprietário. Você deve fornecer sua própria cópia obtida legalmente.

## Sobre o jogo

**Climb! A Mountain in Your Pocket** é um jogo de escalada desafiador, com controles fáceis de aprender e difíceis de dominar. Controle cada mão separadamente, balance nas rochas, use o impulso para saltar, administre a energia e encontre um caminho seguro até o topo.

<p align="center">
  <a href="https://play.google.com/store/apps/details?id=com.IvanAF.ClimbAMIYPfree">
    <img src="https://play-lh.googleusercontent.com/mhu3d320uJKZWnxMcenRkuwexh5Xm1MeVKSgjRTw_JK7fWTJ2Mjnsr9Ta-VgJOuslHiWY4NOCwgU4_5UWoFI1A8=w1052-h592" alt="Gameplay de Climb! A Mountain in Your Pocket" width="760">
  </a>
  <br>
  <sub>Imagem oficial do gameplay — clique para visitar o jogo no Google Play.</sub>
</p>

O jogo original foi criado por **Ivan Alcaide Ferrer** usando o **GameMaker**.

- [Página oficial no Google Play](https://play.google.com/store/apps/details?id=com.IvanAF.ClimbAMIYPfree)
- [Showcase oficial do GameMaker](https://gamemaker.io/en/showcase/climb-a-mountain-in-your-pocket)

## Detalhes do port

- Versão Android do GameMaker executada no Linux através do GMLoader
- Projetado para portáteis ARM compatíveis com PortMaster
- Testado no R36S com ArkOS, processador RK3326 e GPU Mali-G31 MP2
- Suporte aos controles do portátil
- Otimizações e correções para AArch64
- Tratamento de anúncios que poderiam impedir a continuação do jogo
- Nenhum dado proprietário do jogo incluído
- Dados de salvamento armazenados separadamente dos arquivos originais

## Requisitos

- Um portátil compatível com PortMaster
- PortMaster instalado e atualizado
- Uma cópia Android de **Climb! A Mountain in Your Pocket**, versão **6.0.7**, em formato APK, XAPK ou ZIP, obtida legalmente
- Espaço livre suficiente para o port e os dados do jogo

## Instalação

### 1. Baixe o port

Baixe o pacote mais recente na seção **Releases** deste repositório. Extraia o conteúdo e copie os arquivos para a pasta `ports` do cartão SD utilizado pelo portátil.

> Baixar este repositório não fornece o jogo. O pacote contém somente os arquivos criados ou distribuídos para compatibilidade com o PortMaster.

### 2. Obtenha a versão correta do jogo

Obtenha legalmente a versão Android **6.0.7** de **Climb! A Mountain in Your Pocket**. O instalador automático aceita os seguintes formatos:

```text
.apk
.xapk
.zip
```

- O jogo não está incluído no repositório ou no pacote do port.
- Este projeto não fornece links não oficiais para os arquivos do jogo.
- Não publique nem anexe APK, XAPK ou ZIP do jogo em commits, Issues ou Releases.
- Outras versões podem não funcionar com este port.

### 3. Coloque o arquivo em `gamedata`

Copie o APK, XAPK ou ZIP da versão **6.0.7** para:

```text
ports/climb_amy/gamedata/
```

Você não precisa extrair nem renomear o arquivo. Ele pode manter o nome original.

Exemplo:

```text
ports/
├── climb_amy/
│   ├── gamedata/
│   │   └── arquivo-do-jogo.xapk
│   ├── libs/
│   └── controls.gptk
└── Climb! AMiYP.sh
```

> Mantenha apenas um pacote do jogo dentro de `gamedata` durante a instalação.

### 4. Inicie o jogo

Ejete o cartão SD com segurança, insira-o no portátil e abra **Climb! A Mountain in Your Pocket** na seção Ports.

Na primeira inicialização, o port localizará automaticamente o arquivo dentro de `gamedata`, fará a extração, selecionará os dados necessários e preparará o jogo. Ao terminar, o jogo será aberto automaticamente.

A primeira inicialização pode demorar mais do que as seguintes. Não desligue o aparelho durante a extração.

Nas próximas vezes, o jogo abrirá normalmente sem repetir todo o processo.

Se o jogo retornar ao menu, confira:

- se o pacote está dentro de `ports/climb_amy/gamedata/`;
- se o arquivo é APK, XAPK ou ZIP;
- se o jogo corresponde à versão Android `6.0.7`;
- se existe apenas um pacote do jogo dentro de `gamedata`;
- se o arquivo terminou de ser copiado e não está corrompido;
- se todo o pacote do port foi extraído corretamente na pasta `ports`.

## Controles

O jogo utiliza ações separadas para as mãos esquerda e direita. Segure o botão de uma mão para agarrar a rocha, solte para largá-la e combine as duas mãos com o impulso do personagem para balançar e saltar.

| Ação | Controle |
| --- | --- |
| Mão esquerda / agarrar | Botão de ação esquerdo |
| Mão direita / agarrar | Botão de ação direito |
| Navegar nos menus | Direcional / Analógico |
| Confirmar | Botão de confirmação |
| Voltar | Botão de voltar |
| Sair do port | Combinação de saída do PortMaster |

## Compatibilidade

| Aparelho / sistema | Situação |
| --- | --- |
| R36S + ArkOS | Testado |
| RK3326 + Mali-G31 MP2 | Testado |
| Outros aparelhos ARM com PortMaster | Pode funcionar; testes são bem-vindos |

## Solução de problemas

### O jogo retorna ao menu

- Confirme que existe um APK, XAPK ou ZIP dentro de `ports/climb_amy/gamedata/`.
- Confirme que o arquivo corresponde à versão Android `6.0.7`.
- Remova pacotes duplicados e mantenha somente um arquivo do jogo em `gamedata`.
- Copie o pacote novamente caso ele esteja incompleto ou corrompido.
- Atualize o PortMaster e seus runtimes.
- Consulte o log gerado após tentar iniciar o port.

### Os controles não respondem

- Confirme que `controls.gptk` existe na pasta do port.
- Restaure a configuração original dos controles presente no pacote da Release.
- Desconecte controles USB incompatíveis e teste os controles do portátil.

### A imagem está distorcida ou o desempenho está ruim

- Utilize o sistema e a configuração gráfica recomendados para o aparelho.
- Feche serviços em segundo plano antes de iniciar o jogo.
- Ao reportar, informe o modelo do aparelho e envie o log completo.

## Relatórios de erros

Antes de abrir uma Issue, confirme que você está usando a versão mais recente do port e do PortMaster, que os dados do jogo foram obtidos legalmente e copiados corretamente e que o problema pode ser reproduzido.

Não envie APKs, XAPKs, assets extraídos ou outros arquivos protegidos em uma Issue.

## Créditos

- **Ivan Alcaide Ferrer** — jogo e arte originais
- **YoYo Games** — GameMaker
- **Colaboradores do GMLoader** — camada de compatibilidade do GameMaker Android
- **Comunidade PortMaster** — plataforma, ferramentas, runtimes e documentação
- **Lucas Soares** — port e configuração para PortMaster

## Licença

Os scripts, configurações, patches e documentos originais criados especificamente para este port são disponibilizados sob a [Licença MIT](LICENSE), salvo indicação diferente em algum arquivo.

A Licença MIT aplica-se somente ao trabalho original deste port. Ela não se aplica ao jogo original, runtime do GameMaker, GMLoader, bibliotecas de terceiros, arte, áudio, marcas ou dados proprietários.

## Aviso legal

Este é um projeto de compatibilidade não oficial, criado por fãs. Não possui afiliação, patrocínio, aprovação ou endosso de Ivan Alcaide Ferrer, YoYo Games ou das distribuidoras originais.

Todos os nomes, marcas, artes, áudios, códigos e assets do jogo pertencem aos respectivos proprietários. Apoie o desenvolvedor adquirindo o jogo por uma loja oficial.

<p align="right"><a href="#english">Go to English →</a></p>

---

<a id="english"></a>

# 🇺🇸 English

An unofficial PortMaster port of the Android release of **Climb! A Mountain in Your Pocket**. The GameMaker runtime is launched on Linux through **GMLoader**, making the game playable on compatible ARM handhelds such as the **R36S**.

> **BYO-data:** This repository does not include the game, APK, XAPK, copyrighted assets, or any other proprietary game data. You must provide your own legally obtained copy.

## About the game

**Climb! A Mountain in Your Pocket** is a challenging climbing game with controls that are easy to learn and difficult to master. Control each hand independently, swing from the rocks, use your momentum to jump, manage your stamina, and find a safe route toward the summit.

<p align="center">
  <a href="https://play.google.com/store/apps/details?id=com.IvanAF.ClimbAMIYPfree">
    <img src="https://play-lh.googleusercontent.com/mhu3d320uJKZWnxMcenRkuwexh5Xm1MeVKSgjRTw_JK7fWTJ2Mjnsr9Ta-VgJOuslHiWY4NOCwgU4_5UWoFI1A8=w1052-h592" alt="Climb! A Mountain in Your Pocket gameplay" width="760">
  </a>
  <br>
  <sub>Official gameplay screenshot — click the image to visit the game on Google Play.</sub>
</p>

The original game was created by **Ivan Alcaide Ferrer** using **GameMaker**.

- [Official Google Play page](https://play.google.com/store/apps/details?id=com.IvanAF.ClimbAMIYPfree)
- [Official GameMaker showcase](https://gamemaker.io/en/showcase/climb-a-mountain-in-your-pocket)

## Port details

- Android GameMaker release running on Linux through GMLoader
- Designed for PortMaster-compatible ARM handhelds
- Tested on R36S with ArkOS, RK3326 processor, and Mali-G31 MP2 graphics
- Handheld controls supported
- AArch64 optimizations and fixes
- Ad handling fix for situations that could prevent gameplay from continuing
- No proprietary game data included
- Save data is stored separately from the original game files

## Requirements

- A PortMaster-compatible handheld
- PortMaster installed and updated
- A legally obtained Android copy of **Climb! A Mountain in Your Pocket**, version **6.0.7**, in APK, XAPK, or ZIP format
- Enough free storage for the port and the required game data

## Installation

### 1. Download the port

Download the latest port package from this repository's **Releases** page. Extract it and copy the included port files to the `ports` directory of the SD card used by your handheld.

> Downloading this repository does **not** provide the game itself. The port package contains only files created or distributed for PortMaster compatibility.

### 2. Obtain the correct game version

Legally obtain the Android version **6.0.7** of **Climb! A Mountain in Your Pocket**. The automatic installer accepts:

```text
.apk
.xapk
.zip
```

- The game is not included in this repository or port package.
- This project does not provide unofficial links to game files.
- Do not upload or attach the game's APK, XAPK, or ZIP to commits, Issues, or Releases.
- Other game versions may not work with this port.

### 3. Place the file in `gamedata`

Copy the version **6.0.7** APK, XAPK, or ZIP into:

```text
ports/climb_amy/gamedata/
```

You do not need to extract or rename the file. It may keep its original filename.

Example:

```text
ports/
├── climb_amy/
│   ├── gamedata/
│   │   └── game-package.xapk
│   ├── libs/
│   └── controls.gptk
└── Climb! AMiYP.sh
```

> Keep only one game package inside `gamedata` during installation.

### 4. Launch the game

Safely eject the SD card, insert it into your handheld, and start **Climb! A Mountain in Your Pocket** from the Ports section.

On the first launch, the port will automatically locate the file inside `gamedata`, extract it, select the required data, and prepare the game. The game will open automatically when the process is complete.

The first launch may take longer than subsequent launches. Do not turn off the device during extraction.

After the initial setup, the game will start normally without repeating the full process.

If the game returns immediately to the menu, check:

- the package is inside `ports/climb_amy/gamedata/`;
- the file is an APK, XAPK, or ZIP;
- the game is Android version `6.0.7`;
- only one game package is present inside `gamedata`;
- the file finished copying and is not corrupted;
- the complete port package was correctly extracted into `ports`.

## Controls

The game uses separate actions for the climber's left and right hands. Hold a hand button to grip a rock, release it to let go, and combine both hands with the character's momentum to swing and jump.

| Action | Control |
| --- | --- |
| Left hand / grip | Left-hand action button |
| Right hand / grip | Right-hand action button |
| Navigate menus | D-pad / Analog stick |
| Confirm | Confirm button |
| Back | Back button |
| Exit the port | PortMaster exit combination |

## Compatibility

| Device / system | Status |
| --- | --- |
| R36S + ArkOS | Tested |
| RK3326 + Mali-G31 MP2 | Tested |
| Other PortMaster ARM devices | May work; testing is welcome |

## Troubleshooting

### The game returns to the menu

- Confirm that an APK, XAPK, or ZIP exists inside `ports/climb_amy/gamedata/`.
- Confirm that the file is the Android version `6.0.7`.
- Remove duplicate packages and keep only one game file in `gamedata`.
- Copy the package again if it is incomplete or corrupted.
- Update PortMaster and its runtimes.
- Check the log generated after attempting to launch the port.

### Controls do not respond

- Confirm that `controls.gptk` exists inside the port folder.
- Restore the original control configuration from the Release package.
- Disconnect unsupported USB controllers and test the handheld controls.

### The image is distorted or performance is poor

- Use the recommended system image and graphics configuration for your device.
- Close background services before launching the game.
- Include the device model and complete log when reporting the issue.

## Bug reports

Before opening an Issue, verify that you are using the latest port and PortMaster versions, your game data was legally obtained and correctly copied, and the problem can be reproduced.

Do not upload APKs, XAPKs, extracted game assets, or other copyrighted files to an Issue.

## Credits

- **Ivan Alcaide Ferrer** — original game and artwork
- **YoYo Games** — GameMaker
- **GMLoader contributors** — GameMaker Android compatibility layer
- **PortMaster community** — platform, tools, runtimes, and documentation
- **Lucas Soares** — PortMaster port and configuration

## License

The original scripts, configuration files, patches, and documentation created specifically for this port are licensed under the [MIT License](LICENSE), unless a file states otherwise.

The MIT License applies only to original porting work contained in this repository. It does not apply to the original game, GameMaker runtime, GMLoader, third-party libraries, artwork, audio, trademarks, or proprietary game data.

## Legal notice

This is an unofficial, fan-made compatibility project. It is not affiliated with, sponsored by, approved by, or endorsed by Ivan Alcaide Ferrer, YoYo Games, or the original publishers and distributors.

All game names, trademarks, artwork, audio, code, and assets belong to their respective owners. Support the original developer by obtaining the game through an official store.

<p align="right"><a href="#portugues">← Voltar ao Português</a></p>
