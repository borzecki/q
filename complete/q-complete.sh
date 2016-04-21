_q_completion() {
    local cur=${COMP_WORDS[COMP_CWORD]}
    local prev=${COMP_WORDS[COMP_CWORD-1]}
    case "$cur" in
        -) COMPREPLY=( $(compgen -W "-e -o -l"));;
        -*) COMPREPLY=( $(compgen -W "--search-engine --search-option --list-engines --help" -- "$cur"));;
    esac

    case "$prev" in
            -e|--search-engine) COMPREPLY=( $(compgen -W "$(q -l)" -- "$cur") ) ;;
    esac
} && complete -o filenames -F _q_completion q
