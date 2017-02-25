function sendPost() {
    // This is code to sned the post
    var path = "postHtml"
    var params = "html=<html><head><title>Look at this</title></head><body><p>Hey</p></body></html>"

    var form = document.createElement('form');
    form.setAttribute('method', 'post')
    form.setAttribute('action', '/postHtml')
    document.body.appendChild(form)
    form.submit()
}
