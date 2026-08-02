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
- APK Android de **Climb! A Mountain in Your Pocket**, versão **6.0.7**, obtido legalmente
- Espaço livre suficiente para o port e os dados do jogo

## Instalação

### 1. Baixe o port

Baixe o pacote mais recente na seção **Releases** deste repositório. Extraia o conteúdo e copie os arquivos para a pasta `ports` do cartão SD utilizado pelo portátil.

> Baixar este repositório não fornece o jogo. O pacote contém somente os arquivos criados ou distribuídos para compatibilidade com o PortMaster.

### 2. Forneça seu próprio APK

Obtenha legalmente o APK Android de **Climb! A Mountain in Your Pocket, versão 6.0.7**.

- O APK não está incluído no repositório ou no pacote do port.
- Este projeto não fornece links não oficiais para o APK.
- Não publique nem anexe o APK em commits, Issues ou Releases.
- Outras versões podem não funcionar com este port.

### 3. Renomeie o APK

Ative a exibição das extensões de arquivo no computador e renomeie o APK exatamente para:

```text
climb64.apk
```

O nome deve estar em letras minúsculas. Verifique se o Windows não criou acidentalmente `climb64.apk.apk`.

### 4. Copie o APK para `gamedata`

Copie `climb64.apk` para:

```text
climb_amy/gamedata/
```

O caminho completo precisa ser:

```text
ports/climb_amy/gamedata/climb64.apk
```

Não extraia o APK e não o coloque ao lado do script de inicialização.

### 5. Confira a estrutura

```text
ports/
├── climb_amy/
│   ├── gamedata/
│   │   └── climb64.apk
│   ├── libs/
│   └── controls.gptk
└── Climb! AMiYP.sh
```

### 6. Inicie o jogo

Ejete o cartão SD com segurança, insira-o no portátil e abra **Climb! A Mountain in Your Pocket** na seção Ports. A primeira inicialização pode levar um pouco mais de tempo.

Se o jogo retornar imediatamente ao menu, confira:

- se a pasta se chama exatamente `climb_amy`;
- se a subpasta se chama exatamente `gamedata`;
- se o arquivo se chama exatamente `climb64.apk`;
- se o APK corresponde à versão `6.0.7`;
- se o APK não foi extraído nem deixado dentro de ZIP/XAPK;
- se todo o pacote foi extraído na pasta `ports`.

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

- Confirme que existe `ports/climb_amy/gamedata/climb64.apk`.
- Confirme que o APK é a versão Android `6.0.7` e não foi extraído.
- Verifique se o arquivo não foi nomeado `climb64.apk.apk`.
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
- A legally obtained Android APK of **Climb! A Mountain in Your Pocket**, specifically version **6.0.7**
- Enough free storage for the port and the required game data

## Installation

### 1. Download the port

Download the latest port package from this repository's **Releases** page. Extract it and copy the included port files to the `ports` directory of the SD card used by your handheld.

> Downloading this repository does **not** provide the game itself. The port package contains only files created or distributed for PortMaster compatibility.

### 2. Provide your own game APK

Obtain your own legal copy of **Climb! A Mountain in Your Pocket for Android, version 6.0.7**.

- The APK is not included in this repository or port package.
- This project does not provide unofficial APK download links.
- Do not upload or attach the APK to commits, Issues, or Releases.
- Other game versions may not work with this port.

### 3. Rename the APK

Make file extensions visible on your computer and rename the APK exactly to:

```text
climb64.apk
```

The filename must be lowercase. Make sure Windows did not create `climb64.apk.apk`.

### 4. Copy the APK into `gamedata`

Copy `climb64.apk` into:

```text
climb_amy/gamedata/
```

The complete path must be:

```text
ports/climb_amy/gamedata/climb64.apk
```

Do not extract the APK or place it beside the launcher script.

### 5. Check the final structure

```text
ports/
├── climb_amy/
│   ├── gamedata/
│   │   └── climb64.apk
│   ├── libs/
│   └── controls.gptk
└── Climb! AMiYP.sh
```

### 6. Launch the game

Safely eject the SD card, insert it into the handheld, and start **Climb! A Mountain in Your Pocket** from the Ports section. The first launch may take a little longer.

If the game returns immediately to the menu, check:

- the folder is named exactly `climb_amy`;
- the subfolder is named exactly `gamedata`;
- the file is named exactly `climb64.apk`;
- the APK is version `6.0.7`;
- the APK was not extracted or left inside a ZIP/XAPK;
- the complete port package was extracted into `ports`.

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

- Confirm that `ports/climb_amy/gamedata/climb64.apk` exists.
- Confirm that it is Android version `6.0.7` and was not extracted.
- Check that the file was not accidentally named `climb64.apk.apk`.
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
