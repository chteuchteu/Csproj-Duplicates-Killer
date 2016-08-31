# Csproj Duplicates Killer
Find and removes duplicates `<Content Include="..." />` entries in any csproj file.
 
## Usage

```bash
chmod u+x main.py && python3 main.py
```

Sample output:

    Found duplicate     <Content Include="Areas\Shared\Views\Partial\DisplayTemplates\DisplayBase.cshtml" />
    Found duplicate     <Content Include="Areas\Shared\Views\Partial\DisplayTemplates\Decimal.cshtml" />
    Found duplicate     <Content Include="Areas\Shared\Views\Partial\_FlashMessages.cshtml" />
    Successfully removed 3 duplicates lines
    Result csproj has been written to "MyProject.csproj.new". Please review changes and update "MyProject.csproj".
