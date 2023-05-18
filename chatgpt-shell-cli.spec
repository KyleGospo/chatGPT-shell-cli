%global execname chatgpt

Name:           %{execname}-shell-cli
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Simple shell script to use OpenAI's ChatGPT and DALL-E from the terminal. No Python or JS required. 

License:        MIT
URL:            https://github.com/KyleGospo/chatGPT-shell-cli/

VCS:            {{{ git_dir_vcs }}}
Source:         {{{ git_dir_pack }}}
BuildArch:      noarch

Requires:       curl
Requires:       jq
Requires:       xdg-utils
Requires:       ImageMagick

BuildRequires:  systemd-rpm-macros

%description
A simple, lightweight shell script to use OpenAI's chatGPT and DALL-E from the terminal without installing python or node.js. The script uses the official ChatGPT model gpt-3.5-turbo with the OpenAI API endpoint /chat/completions. You can also use the new gpt-4 model, if you have access.

# Disable debug packages
%define debug_package %{nil}

%prep
{{{ git_dir_setup_macro }}}
mv %{execname}.sh %{execname}
# Replace open image command with xdg-open for linux systems
sed -i 's/open "\${image_url}"/xdg-open "\${image_url}"/g' %{execname}

%install
install -Dm 755 %{execname} -t %{buildroot}%{_bindir}

%post
echo "The OPENAI_KEY environment variable containing your key is necessary for %{name} to function."
echo -e "Add the line below to your shell profile with a valid key:\n"
echo "export OPENAI_KEY=\"your_key_here\""
echo -e "\nIf needed, detailed instructions are available:\nhttps://github.com/0xacx/chatGPT-shell-cli/tree/main#manual-installation"

%preun

%postun

%files
%license LICENSE
%doc README.md
%{_bindir}/%{execname}

%changelog
{{{ git_dir_changelog }}}