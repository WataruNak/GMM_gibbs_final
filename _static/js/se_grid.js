// アイテムのリストを取得
const items = [...document.querySelectorAll(".item")];
let img_category_list = js_vars.img_category_list;
let imgcatpath_list = js_vars.imgcatpath_list;
let default_name_value = js_vars.default_name_value;
let img_choice = js_vars.img_choice;
let choice_cat_fields = [
  document.getElementById("s_choice0"),
  document.getElementById("s_choice1"),
  document.getElementById("s_choice2"),
  document.getElementById("s_choice3"),
  document.getElementById("s_choice4"),
]
let stimuli_img_id_list = []
for (let d=0; d<40; d++) {
  stimuli_img_id_list.push("stimuli" + d)
}

let choice_img_class_list = [
  "selected0", "selected1", "selected2", "selected3", "selected4"
]
let role = js_vars

window.onload = function() {
  for (let a=0; a<40; a++) {
    document.getElementById(imgcatpath_list[a]).value = String(img_category_list[a]);
  };
  document.getElementById("name_order").value = default_name_value;
  for (let b=0; b<5; b++) {
    document.getElementById(stimuli_img_id_list[img_choice[b]]).classList.add(choice_img_class_list[b])
    document.getElementById(String(img_choice[b])).classList.add(choice_img_class_list[b]);
  };
  if (role == "speaker") {
    for (let c=0; c<40; c++) {
      choice_cat_fields[c].value = String(img_category_list[img_choice[c]])
    };
  };  
};

let img_cat_list = new Array(40);
  for (let n=0; n<40; n++) {
    img_cat_list[n] = document.getElementById(imgcatpath_list[n]);
  };

let box_list = new Array(6);
  for (let m=0; m<6; m++) {
    let boxpath = "box" + m;
    box_list[m] = document.getElementById(boxpath)
  };

let boxchildren_list = new Array(6);
  for (let mc=0; mc<6; mc++) {
    let boxchildrenpath = "box" + mc + "_children";
    boxchildren_list[mc] = document.getElementById(boxchildrenpath);
  };

console.log("hello");


let el = document.getElementById('names');
let sortablename = Sortable.create(el, {
  onChange: function (evt) {
    let sorted_order = sortablename.toArray()
    document.getElementById('name_order').value = sortablename.toArray().join(',');
    for (let j=0; j<6; j++) {
      if (box_list[j].childElementCount>0) {
        let childidlist = [];
        for (let jj=0; jj< box_list[j].childElementCount; jj++) {
          let stimid = Number(box_list[j].children[jj].id);
          let catofimg_namechange = Number(sorted_order[j].substr(-1));
          img_cat_list[stimid].value = catofimg_namechange;
          childidlist.push(String(stimid));
        };
        boxchildren_list[j].value = childidlist.join(",");
      } else {
        boxchildren_list[j].value = "999"
      };
    };
    if (role == "speaker") {
      for (let l=0; l<5; l++) {
        if (
          choice_cat_fields[l].value != document.getElementById(String(img_choice[l]))
          ) {
            choice_cat_fields[l].value = document.getElementById(String(img_choice[l]))
          };
        }
    }
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
  let catofimg = Number(categoryorder[Number(e.currentTarget.id.substr(-1))].substr(-1));
  img_cat_list[imgid4cat].value = String(catofimg);
  for (let k=0; k<6; k++) {
    if (box_list[k].childElementCount>0) {
      let childidlist2 = [];
      for (let kk=0; kk<box_list[k].childElementCount; kk++) {
        let stimid2 = Number(box_list[k].children[kk].id);
        childidlist2.push(String(stimid2));
      };
      boxchildren_list[k].value = childidlist2.join(",");
    } else {
      boxchildren_list[k].value = "999"
    };
  };
  if (role == "speaker") {
    for (let m=0; m<5; m++) {
      if (
        choice_cat_fields[m].value != document.getElementById(String(img_choice[m]))
        ) {
          choice_cat_fields[m].value = document.getElementById(String(img_choice[m]))
        };
      }
  }
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

