# koceti_ament_copyright

Adds entrypoints for the `ament_copyright` utility to allow checking KOCETI's headers for copyright info and proprietary licenses.

## How to Use

### Installation

Clone and build this repo so it's available in your ROS package paths.

### Command Line

To add missing KOCETI-proprietary license headers to all files in the current directory, run the command below (`koceti` sets KOCETI Corp. as the copyright holder, and `koceti_proprietary` uses our closed-source proprietary license template).

```
ament_copyright --add-missing koceti_proprietary koceti .
```

This will insert the following license header in source code files that do not already have a license header that `ament_copyright` recognizes:

```
// Copyright 2022 KOCETI Corp.
// All rights reserved.
//
// Unauthorized copying of this code base via any medium is strictly prohibited.
// Proprietary and confidential.
```

### pre-commit

Here is a basic `.pre-commit-config.yaml` file that automatically inserts the KOCETI proprietary license in source code files:

```
repos:
  - repo: local
    hooks:
      - id: ament_copyright
        name: ament_copyright
        language: system
        entry: ament_copyright
        args: ['--add-missing', 'koceti', 'koceti_proprietary', '.']
```
