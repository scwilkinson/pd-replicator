SCRIPT_HTML = '''
<script>
    function copyTextToClipboard(object) {
        var textArea = document.createElement("textarea");
        textArea.id = "copy_text_area";
        textArea.value = object.getAttribute('text-to-copy');
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        document.execCommand("copy");
        document.body.removeChild(textArea);

        object.style.backgroundColor = "var(--jp-success-color1)"
        object.style.color = "var(--jp-inverse-ui-font-color1)"

        setTimeout(function () {
            object.style.backgroundColor = "var(--jp-layout-color2)";
            object.style.color = "var(--jp-ui-font-color1)";
        }, 1000);
    }
</script>
'''

BUTTON_HTML = '''
<button id="my-id" class="jupyter-button widget-button" text-to-copy="{}" onclick="copyTextToClipboard(this)">
    Copy
</button>
'''