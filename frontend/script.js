const apiUrl = "http://127.0.0.1:8000/books";

document.addEventListener("DOMContentLoaded", () => {
  populateYears(); // Yılları ekle
  loadBooks();

  const form = document.getElementById("bookForm");
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const id = document.getElementById("bookId").value;
    const title = document.getElementById("title").value;
    const author = document.getElementById("author").value;
    const year = parseInt(document.getElementById("year").value);

    const book = { title, author, year };

    if (id) {
      await fetch(`${apiUrl}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(book),
      });
    } else {
      await fetch(apiUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(book),
      });
    }

    form.reset();
    loadBooks();
  });
});

// 🔽 Yıl seçim kutusuna öneri yıllarını ekler
function populateYears() {
  const datalist = document.getElementById("yearOptions");
  const currentYear = new Date().getFullYear();
  for (let y = currentYear; y >= 1980; y--) {
    const option = document.createElement("option");
    option.value = y;
    datalist.appendChild(option);
  }
}

async function loadBooks() {
  const res = await fetch(apiUrl);
  const books = await res.json();

  const tableBody = document.getElementById("bookTableBody");
  tableBody.innerHTML = "";

  books.forEach((book) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${book.title}</td>
      <td>${book.author}</td>
      <td>${book.year}</td>
      <td class="action-buttons">
        <button class="edit-btn" onclick="editBook(${book.id}, '${book.title}', '${book.author}', ${book.year})">Düzenle</button>
        <button class="delete-btn" onclick="deleteBook(${book.id})">Sil</button>
      </td>
    `;
    tableBody.appendChild(tr);
  });
}

function editBook(id, title, author, year) {
  document.getElementById("bookId").value = id;
  document.getElementById("title").value = title;
  document.getElementById("author").value = author;
  document.getElementById("year").value = year;
}

async function deleteBook(id) {
  await fetch(`${apiUrl}/${id}`, { method: "DELETE" });
  loadBooks();
}
