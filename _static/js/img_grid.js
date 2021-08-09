// アイテムのリストを取得
const items = [...document.querySelectorAll(".item")];
const imgorder = js_vars.id_order;
let imgcatexample = js_vars.imgcatex;

window.onload = function() {
  alert("ページが読み込まれました！");
};

let img_cat_list = new Array(40);
  for (let n=0; n<40; n++) {
    let path = "img" + n + "_cat";
    img_cat_list[n] = document.getElementById(path);
  };

let box_list = new Array(6);
  for (let m=0; m<6; m++) {
    let boxpath = "box" + (m+1);
    box_list[m] = document.getElementById(boxpath)
  };

console.log(document.getElementById("img0_cat"));
for (const jjj in document.getElementById("names").children) {
  console.log(jjj);
};
console.log(img_cat_list[0].value);
console.log("hello");
console.log(document.getElementById("1"));
console.log(document.getElementById("1").id);
console.log(parseInt(document.getElementById("1").id, 10));
console.log(img_cat_list[parseInt(document.getElementById("1").id, 10)].value);  


let el = document.getElementById('names');
let sortablename = Sortable.create(el, {
  onChange: function (evt) {
    let sorted_order = sortablename.toArray()
    document.getElementById('name_order').value = sortablename.toArray().join(',');
    for (let j=0; j<6; j++) {
      if (box_list[j].hasChildNodes) {
        for (let jj=0; jj< box_list[j].childElementCount; jj++) {
          let stimid = Number(box_list[j].children[jj].id);
          console.log(box_list[j].children[jj]);
          console.log(stimid);
          let catofimg_namechange = Number(sorted_order[j].substr(-1));
          console.log(catofimg_namechange);
          img_cat_list[stimid].value = catofimg_namechange;
          console.log(img_cat_list[stimid]);
          console.log(img_cat_list[stimid].value);
        }
      }
    };
  }
});


// ドラッグ開始イベントを定義
const handleDragStart = (e) => {
  e.currentTarget.classList.add("dragging");
  e.dataTransfer.effectAllowed = "move";
  let { id } = e.currentTarget;
  e.dataTransfer.setData("application/json", JSON.stringify({ id }));
};

// ドラッグ終了イベントを定義
const handleDragEnd = (e) => e.currentTarget.classList.remove("dragging");

// アイテムにイベントを登録
for (const item of items) {
  item.addEventListener("dragstart", handleDragStart, false);
  item.addEventListener("dragend", handleDragEnd, false);
}

// 要素が重なった際のイベントを定義
const handleDragEnter = (e) => {
  // 子要素へのドラッグを制限
  if (
    [...e.currentTarget.classList].includes("item")    
    ) {
      e.dataTransfer.dropEffect = "none";
    return;
  };
  e.currentTarget.classList.add("over");
};

// 要素が離れた際のイベントを定義
const handleDragLeave = (e) => e.currentTarget.classList.remove("over");

// 要素が重なっている最中のイベントを定義
const handleDragOver = (e) => {
  // 要素が重なった際のブラウザ既定の処理を変更
  e.preventDefault();

  // 子要素へのドラッグを制限
  if (
    [...e.currentTarget.classList].includes("item") 
    ) {
    e.dataTransfer.dropEffect = "none";
    return;
  };
  // ドロップ効果の設定
  e.dataTransfer.dropEffect = "move";
};

// 要素がドロップされた際のイベントを定義
const handleDrop = (e) => {
  // 要素がドロップされた際のブラウザ既定の処理を変更
  e.preventDefault();
  e.currentTarget.classList.remove("over");
  // ブラウザ外からのファイルドロップを制限
  if (e.dataTransfer.files.length > 0) {
    return;
  };
  // 転送データの取得
  let { id } = JSON.parse(e.dataTransfer.getData("application/json"));
  // ドロップ先に要素を追加する
  e.currentTarget.appendChild(document.getElementById(id));
  let imgid4cat = Number(document.getElementById(id).id);
  let categoryorder = document.getElementById("name_order").value.split(',');
  console.log(document.getElementById(id));
  console.log(categoryorder);
  console.log(e.currentTarget.id);
  console.log(categoryorder[Number(e.currentTarget.id.substr(-1))-1]);
  let catofimg = Number(categoryorder[Number(e.currentTarget.id.substr(-1))-1].substr(-1));
  console.log(catofimg);
  console.log(imgid4cat);
  console.log(img_cat_list[imgid4cat]);
  img_cat_list[imgid4cat].value = String(catofimg);
  console.log(img_cat_list[imgid4cat].value);
  if (
    document.getElementById('img0_cat').value != "0" &&
    document.getElementById('img1_cat').value != "0" &&
    document.getElementById('img2_cat').value != "0" &&
    document.getElementById('img3_cat').value != "0" &&
    document.getElementById('img4_cat').value != "0" &&
    document.getElementById('img5_cat').value != "0" &&
    document.getElementById('img6_cat').value != "0" &&
    document.getElementById('img7_cat').value != "0" &&
    document.getElementById('img8_cat').value != "0" &&
    document.getElementById('img9_cat').value != "0" &&
    document.getElementById('img10_cat').value != "0" &&
    document.getElementById('img11_cat').value != "0" &&
    document.getElementById('img12_cat').value != "0" &&
    document.getElementById('img13_cat').value != "0" &&
    document.getElementById('img14_cat').value != "0" &&
    document.getElementById('img15_cat').value != "0" &&
    document.getElementById('img16_cat').value != "0" &&
    document.getElementById('img17_cat').value != "0" &&
    document.getElementById('img18_cat').value != "0" &&
    document.getElementById('img19_cat').value != "0" &&
    document.getElementById('img20_cat').value != "0" &&
    document.getElementById('img21_cat').value != "0" &&
    document.getElementById('img22_cat').value != "0" &&
    document.getElementById('img23_cat').value != "0" &&
    document.getElementById('img24_cat').value != "0" &&
    document.getElementById('img25_cat').value != "0" &&
    document.getElementById('img26_cat').value != "0" &&
    document.getElementById('img27_cat').value != "0" &&
    document.getElementById('img28_cat').value != "0" &&
    document.getElementById('img29_cat').value != "0" &&
    document.getElementById('img30_cat').value != "0" &&
    document.getElementById('img31_cat').value != "0" &&
    document.getElementById('img32_cat').value != "0" &&
    document.getElementById('img33_cat').value != "0" &&
    document.getElementById('img34_cat').value != "0" &&
    document.getElementById('img35_cat').value != "0" &&
    document.getElementById('img36_cat').value != "0" &&
    document.getElementById('img37_cat').value != "0" &&
    document.getElementById('img38_cat').value != "0" &&
    document.getElementById('img39_cat').value != "0"
    ) {
    document.getElementById("button_to_se").style.visibility = "visible";
  };
}

// ドロップ先のリストを取得
const boxes = [...document.querySelectorAll(".box")];

// ドロップ先にイベントを登録
for (const box of boxes) {
  box.addEventListener("dragenter", handleDragEnter, false);
  box.addEventListener("dragleave", handleDragLeave, false);
  box.addEventListener("dragover", handleDragOver, false);
  box.addEventListener("drop", handleDrop, false);
}

