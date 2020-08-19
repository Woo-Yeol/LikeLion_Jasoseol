// 요소 선택
const targetForm = document.querySelector('.jss_content_form')
const counted_text = document.querySelector('.counted_text')

// 이벤트 핸들러
targetForm.addEventListener("keyup", function(){
    counted_text.innerHTML = targetForm.value.length
})