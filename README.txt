######################################################################################################################

To run functions using powershell scripts the following requirements are necessary.

The script execution function uses the Azure AD module.
Command to install: Install-Module AzureAD

It is necessary to enable the execution of scripts in powershell.
Command to enable: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine.

Note: enabling the permission to execute scripts must be done in a controlled and secure environment.

######################################################################################################################